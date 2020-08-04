from InstagramClass import InstagramBot


def main():
    email = str(input("Email completo: "))
    password = str(input("Senha: "))
    pages_to_like = []
    loop = True

    while loop:
        hashtag = str(input("Nome da página para curtir fotos (enter para finalizar): "))

        if not hashtag:
            loop = False
        else:
            pages_to_like.append(hashtag)

    bot = InstagramBot(email, password)
    bot.login()

    for hashtag in pages_to_like:
        bot.like_photos(hashtag)


if __name__ == '__main__':
    main()
