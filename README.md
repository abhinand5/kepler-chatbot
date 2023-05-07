# Conversational AI Chatbot for Personal Use
This is a conversational AI chatbot that has been trained on a custom knowledge base. The chatbot uses OpenAI's advanced natural language processing technology to understand and respond to user queries in a conversational manner.

## Features
- Can answer a wide range of questions related to the product and the admin panel
- Uses natural language processing to understand user queries and respond in a conversational manner
- Provides detailed information and instructions on how to use the admin panel (might have to increase the allowed output token size for longer responses)
- Can be easily integrated into existing products and services
- Provides a simple `gradio` user interface to interact with the bot.

## Getting Started
To start using the chatbot in demo mode:

```python
# Install poetry package manager
$ pip install poetry
# Install dependencies
$ poetry install
# Launch the demo app (make sure to update the .env file)
$ python demo_app.py
```

If the model is not behaving creative enough try modiying the `temperature` argument of OpenAI.

## Disclaimer
- This required OpenAI API Key, you will be billed for the usage depending on the model chosen and the tokens being processed. 
- Visit the OpenAI pricing page [here](https://openai.com/pricing) to learn more.