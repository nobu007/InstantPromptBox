from instant_prompt_box import InstantPromptBox

if __name__ == "__main__":
    prompt = InstantPromptBox.zoltraak.zoltraak_prompt_fix_code(
        code="test_code", error_message="test_error_message"
    )
    print("prompt:", prompt)
