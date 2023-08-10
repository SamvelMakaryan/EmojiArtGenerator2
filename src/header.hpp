#ifndef HEADER_HPP_
#define HEADER_HPP_

#include <opencv2/opencv.hpp>
#include <string>

struct Color {
    int blue;
    int green;
    int red;
};

void is_empty(const cv::Mat&);
void is_valid_argc(int);
Color getBackgroundColor(const std::string&);
int getEmojiSize(const std::string&);

#endif //HEADER_HPP_
