import tiktoken

class StringHelpers:
    def __init__(self):
        pass

    def num_tokens_from_string(self, content: str, encoding_name: str = None) -> int:
       """Returns the number of tokens in a given text string."""
       if encoding_name is None:
           encoding_name = 'cl100k_base'
       encoding = tiktoken.get_encoding(encoding_name)
       num_tokens = len(encoding.encode(content))
       return num_tokens

