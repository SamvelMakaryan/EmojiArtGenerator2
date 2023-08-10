#include <stdexcept>
#include <sstream>
#include <string>

#include "header.hpp"

Color getBackgroundColor(const std::string& color) {
    Color background_color;
    if (color == "white") {
        background_color = {255, 255, 255};
    } else if (color == "black") {
        background_color = {0, 0, 0};
    } else if (color == "blue") {
        background_color = {255, 0, 0};
    } else if (color == "red") {
        background_color = {0, 0, 255};
    } else if (color == "yellow") {
        background_color = {0, 255, 255};
    } else if (color == "green") {
        background_color = {0, 255, 0};
    } else {
        if (color.front() != '[' || color.back() != ']') {
            throw std::invalid_argument("Unrecognized color : the color should be "
                                        "[black] [blue] [red] [green] [white] [yellow] "
                                        "or in [R,G,B] format\n");
        }
        std::stringstream ss(color);
        ss.ignore();
        std::string tmp_color;
        try {
            std::getline(ss, tmp_color, ',');
            background_color.red = std::stoi(tmp_color);
            std::getline(ss, tmp_color, ',');
            background_color.green = std::stoi(tmp_color);
            std::getline(ss, tmp_color, ',');
            background_color.blue = std::stoi(tmp_color);
        } catch(...) {
            throw std::invalid_argument("Unrecognized color : the color should be "
                                        "[black] [blue] [red] [green] [white] [yellow] "
                                        "or in [R,G,B] format\n");
        }
        if (background_color.red < 0 || background_color.blue < 0 || background_color.green < 0 ||
            background_color.red > 255 || background_color.green > 255 || background_color.blue > 255) {
            throw std::invalid_argument("Invalid color value.\n");
        }
    }
    return background_color;
}