#include <stdexcept>
#include <string>

int getEmojiSize(const std::string& size) {
    int tmp_size;
    try {
        tmp_size = std::stoi(size);
    } catch(...) {
        throw std::invalid_argument("Invalid size value.\n");
    }
    if (tmp_size <= 0) {
        throw std::invalid_argument("Invalid size value.\n");    
    }
    return tmp_size;
}