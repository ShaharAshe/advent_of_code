#include <cstdlib>
#include <fstream>
#include <string>
#include <exception>
#include <iostream>

int count_floars(std::ifstream&);
std::ifstream open_file(const std::string& file_name);

int main(){
    try{
        auto input_file = open_file("./input.txt");
        auto floar_number = count_floars(input_file);
        std::cout << floar_number << std::endl;
        input_file.close();
    } catch (const std::ios_base::failure& e) {
        std::cerr << "I/O Error: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return EXIT_SUCCESS;
}

std::ifstream open_file(const std::string& file_name){
    std::ifstream input_file;
    input_file.open(file_name, std::ios::in);
    if(!input_file)
        throw std::runtime_error("Exception opening/reading file");
    return input_file;
}

int count_floars(std::ifstream& input_file){
    int floar_number = 0;
    char read_char_parenthesis;

    while (input_file >> read_char_parenthesis)
    {
        std::cout << "8" << std::endl;
        switch (read_char_parenthesis)
        {
        case '(':++floar_number;
            break;
        case ')':--floar_number;
            break;
        
        default:
            break;
        }
        std::cout << "7" << std::endl;
    }
    
    return floar_number;
}