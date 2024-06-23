import sys


class Environment:
    @staticmethod
    def set_environemt(env_k, env_v):
        """
            设置用例环境变量
        """
        if not isinstance(sys.path[-1], dict):
            sys.path.append({env_k: env_v})
        else:
            sys.path[-1].update({env_k: env_v})

    @staticmethod
    def get_environment(env_k):
        """
            根据k获取环境变量
        """
        return sys.path[-1].get(env_k)

    @staticmethod
    def get_all_environment():
        """
            获取当前用例所有环境变量
        """
        return sys.path[-1]
