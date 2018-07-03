# See readme.md for instructions on running this code.
import random
from typing import Any, Dict


moria = {
    'comen mortadela y eructan caviar':
        'https://i1.wp.com/blog.elmeme.me/wp-content/uploads/-000//1/2017-11-21_1511278787.png?w=500',
    'se cuelgan de mis tetas':
        'https://i1.wp.com/blog.elmeme.me/wp-content/uploads/-000//1/2017-11-21_1511278779.png?w=500'
}


class FionaHandler(object):

    REQUEST_ERROR_MESSAGE = 'Could not load definition.'
    EMPTY_WORD_REQUEST_ERROR_MESSAGE = 'Please enter a word to define.'
    PHRASE_ERROR_MESSAGE = 'Definitions for phrases are not available.'
    SYMBOLS_PRESENT_ERROR_MESSAGE = 'Definitions of words with symbols are not possible.'

    def usage(self) -> str:
        return "Hola, soy Fiona, la bot de Onapsis."

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        original_content = message['content'].strip()
        bot_response = self.get_bot_define_response(original_content)

        bot_handler.send_reply(message, bot_response)

    def get_bot_define_response(self, original_content: str) -> str:
        if 'moria' in original_content.lower().split():
            return random.choice(moria.items())

        return "Sabía la respuesta, pero pasaron cosas."

handler_class = FionaHandler

