# Chatbot Support In Studying

Welcome to Chatbot Support In Studying!

## Introduction
Chatbot Support In Studying is a cutting-edge artificial intelligence application designed to supports students in studying subjects like Math, Chemistry, History, Science, and many other subjects. It also provides some add-on functions like providing weather information at a specific location or current location (depending on GPS).

## Features
- **Ask about any subjects at school**: Bot can answer any questions about any subjects at school.
- **Interact as human**: Bot can receive and reply user as human language.
- **Multilingual**: Bot have ability to answer question at any languages.
- **Weather information**: Bot have ability to get current position and reply weather status.

## Installation
To install Chatbot Support In Studying, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/ductridev/Chatbot-public
    ```
2. Navigate to the project directory:
    ```
    cd Chatbot-public
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Setting data:
   Add more questions into matching .txt types ```/backend/NLP/data/raw/```
5. Preprocessing:
    ```
    python3 preprocessing.py
    ```
    Or
    ```
    python preprocessing.py
    ```
6. Add more vocab to Word2Vec model:
    ```
    python3 backend/NLP/main/add_more_vocab.py
    ```
    Or
    ```
    python backend/NLP/main/add_more_vocab.py
    ```
7. Training LSTM model:
    ```
    python3 train.py
    ```
    Or
    ```
    python train.py
    ```
8. Setup .env:
    Place all environment variables into .env
9.  Start backend:
    ```
    python3 app.py
    ```
    Or
    ```
    python app.py
    ```
10. Start frontend:
    ```
    cd frontend && npm i && npm start
    ```

## Usage
Here's how to use Chatbot Support In Studying just need 2 steps:

1. Open url is given from frontend (usually is [localhost](http://localhost:3000)):
2. Chat with bot!!!

## Examples
Here are some examples demonstrating the usage of Chatbot Support In Studying:

1. [Example 1: Describe the first example]
2. [Example 2: Describe the second example]
3. [Example 3: Describe the third example]

## Troubleshooting
If you encounter any issues while using Chatbot Support In Studying, consider the following troubleshooting tips:

1. Low ```accuracy``` on re-train model: Try increase data by using data augmentation or duplicate it.
2. High ```accuracy``` but high at ```val_loss```: Overfitting problems, check on Internet about this problem or create a issue with repo url, I will try my best to help you figure out!
3. Any addition problems, please open issues.

## Contributing
We welcome contributions from the community to enhance Chatbot Support In Studying. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create your feature branch:
    ```
    git checkout -b feature/new-feature
    ```
3. Commit your changes:
    ```
    git commit -am 'Add some feature'
    ```
4. Push to the branch:
    ```
    git push https://github.com/ductridev/Chatbot-public feature/new-feature
    ```
5. Submit a pull request.

## License
Chatbot Support In Studying is licensed under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions, suggestions, or feedback, feel free to contact us at [trihd123@gmail.com].

## Acknowledgements
We would like to thank the following individuals and organizations for their contributions to Chatbot Support In Studying:

- [Trịnh Đỗ Duy Hưng](https://github.com/trinhdoduyhungss)

## Disclaimer
Chatbot Support In Studying is provided as is without any guarantees or warranty. The user assumes full responsibility for any consequences resulting from the use of this application.