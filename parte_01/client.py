import urllib.request


def main():
    with urllib.request.urlopen('http://127.0.0.1:5000/tell_time') as response:
        html = response.read()

        dictionary = dict(eval(html))

        print('A resposta do servidor foi a seguinte:')

        for k, v in dictionary.items():
            print('{0}: {1}'.format(k, v))


if __name__ == '__main__':
    main()
