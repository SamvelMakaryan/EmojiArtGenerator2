#include <opencv2/opencv.hpp>
#include <iostream>

void is_empty(const cv::Mat& image) {
    if (image.empty()) {
        std::cerr << "Error: Unable to read the image file." << std::endl;
        exit(-1);
    }
} 

void is_valid_argc(int count) {
    if (count < 3) {
        std::cerr << "Error: too few arguments. " << std::endl;
        std::cout << "Usage: ./EmojiArt <image> <emoji> [emoji size] [background color]" << std::endl;
        exit(-1);
    }
    if (count > 5) {
        std::cerr << "Error: too many arguments. " << std::endl;
        std::cout << "Usage: ./EmojiArt <image> <emoji> [emoji size] [background color]" << std::endl;
        exit(-1);
    }
} 