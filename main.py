
def main():
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
    print(text.split("![image](https://i.imgur.com/zjjcJKZ.png)"))

if __name__ == "__main__":
    main()
