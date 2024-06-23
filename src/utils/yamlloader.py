import yaml


class Yamlloader:
    def load(self, path):
        with open(file=path, mode='r', encoding='utf-8') as f:
            result = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            return result


if __name__ == '__main__':
    res = Yamlloader().load(r'H:\py_home\pythonProject\自动化框架\shopxoWebRunner\data\test_login.yaml')
    print(res['login'][0][4])
    print(type(res['login'][0][4]))
    print(eval(res['login'][0][4]))
    print(type(eval(res['login'][0][4])))
