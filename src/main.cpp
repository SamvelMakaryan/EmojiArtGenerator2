#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

#include "header.hpp"

int main(int argc, char** argv) {
    is_valid_argc(argc);
    int size = 7;
    Color background_color {255, 255, 255};
    std::string image = argv[1];
    cv::Mat inputImage = cv::imread(image);
    is_empty(inputImage);
    cv::Mat emojiImage = cv::imread(argv[2], cv::IMREAD_UNCHANGED);
    is_empty(emojiImage);
    if (argc > 3) {
        size = getEmojiSize(argv[3]);
    }
    if (argc > 4) {
        background_color = getBackgroundColor(argv[4]);
    }
    cv::Size emojiSize(size, size);
    cv::resize(emojiImage, emojiImage, emojiSize);
    cv::Mat outputImage = inputImage.clone();
    outputImage.setTo(cv::Scalar(background_color.blue, background_color.green, background_color.red));
    for (int y = 0; y < inputImage.rows; y += emojiSize.height) {
        for (int x = 0; x < inputImage.cols; x += emojiSize.width) {
            cv::Rect roi(cv::Point(x, y), emojiImage.size());
            if (roi.x >= 0 && roi.y >= 0 && roi.x + roi.width <= outputImage.cols && roi.y + roi.height <= outputImage.rows) {
                cv::Vec3b color = inputImage.at<cv::Vec3b>(y, x);
                cv::Mat shadedEmoji = emojiImage.clone();
                for (int i = 0; i < emojiImage.rows; i++) {
                    for (int j = 0; j < emojiImage.cols; j++) {
                        cv::Vec4b& pixel = shadedEmoji.at<cv::Vec4b>(i, j);
                        if (pixel[3] > 0) { 
                            pixel[0] = cv::saturate_cast<uchar>(pixel[0] + color[0]);
                            pixel[1] = cv::saturate_cast<uchar>(pixel[1] + color[1]);
                            pixel[2] = cv::saturate_cast<uchar>(pixel[2] + color[2]);
                        }
                    }
                }
                cv::Mat overlay = outputImage(roi);
                cv::Mat mask;
                cv::extractChannel(shadedEmoji, mask, 3);
                cv::Mat emoji3Channels;
                cv::cvtColor(shadedEmoji, emoji3Channels, cv::COLOR_BGRA2BGR);
                emoji3Channels.copyTo(overlay, mask);
            }
        }
    }
    std::string output;
    int index = image.size() - 1;
    for (; index >= 0 && image[index] != '.'; --index);
    output = image.substr(index);
    output = "output" + output;
    std::cout << output;
    int specificWidth = 630;
    cv::Mat outputShow = outputImage.clone();
    cv::Size outputSize(specificWidth, specificWidth * outputImage.rows / outputImage.cols);
    cv::resize(outputShow, outputShow, outputSize);
    cv::imwrite(output, outputImage);
}
