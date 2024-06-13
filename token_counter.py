import tiktoken

class token_counter:
    """Class uses openai's tiktoken library.
    Documentation can be found here: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    Make sure to install tiktoken using: pip install --upgrade tiktoken
    """
    
    def __init__(self,) -> None:
        encoding_name:str="cl100k_base"
        self.encoding = tiktoken.get_encoding(encoding_name)
    
    def num_tokens_from_string(self, string: str) -> int:
        """Returns the number of tokens in a text string.

        Example:
            counter = token_counter("cl100k_base")
            counter.num_tokens_from_string("tiktoken is great!")
            returns 6
        """
        num_tokens:int
        if string:
            if string !="":
                num_tokens = len(self.encoding.encode(string))
        return num_tokens

# # Example usage
# counter = token_counter()
# num_tokens = counter.num_tokens_from_string("tiktoken is great!")
# print(num_tokens)
