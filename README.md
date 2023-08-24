LLaMa GUI Interface

LLaMa is a large language model developed by Meta. This GUI interface provides a simple way to run LLaMa on an M1 Max, with options for quickly entering prompts and adjusting basic parameters. This would not be possible without Georgi Gerganov's C/C++ implementation of LLaMa (https://github.com/ggerganov/llama.cpp).

Prerequisites

To use this GUI interface, you will need to follow the steps outlined in https://github.com/ggerganov/llama.cpp, as well as the necessary model files. Instructions for installing and using LLaMa.cpp can be found in the LLaMa.cpp ReadMe.

Usage

To run the GUI interface, simply run the Flask app (defined in app.py). This will open up the interface window, which includes the following options:

Prompt: Enter the text prompt to generate output from
Number of tokens: Select the number of tokens to generate in the output

Once you have selected your options, click the "Submit" button to generate output based on the LLaMa model and parameters you have selected. The generated text will appear in the output field.

Limitations

Note that the LLaMa model used for generation may have limitations in terms of accuracy and bias. Additionally, the GUI interface may have limitations in terms of its usability and performance, depending on your system specifications.

Acknowledgements

This GUI interface is based on the LLaMa library developed by Facebook Research and the LLaMa implementation by Georgi Gerganov. 
