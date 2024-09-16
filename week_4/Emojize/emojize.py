def main():
    import emoji
    inp=input("Input: ")
    emo_text=emoji.emojize(inp,language='alias')
    print(f"Output: {emo_text}")

if __name__ == "__main__":
    main()

