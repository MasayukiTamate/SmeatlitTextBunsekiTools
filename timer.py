from time import monotonic, sleep

def timer():
    start = monotonic()

    def inner(message):
        print(f"{message}: {monotonic() - start:.2f}")

    return inner


if __name__ == "__main__":
    t = timer()
    t("ようこそ世界")
    sleep(3)
    t("ようこそ世界 第２弾")
    sleep(2)
    t("ようこそ世界 第３弾")