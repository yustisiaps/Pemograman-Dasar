class ikan:
    def __init__(var, q):
        var.quest = q
        var.jaw = []
        var.isi = []
        var.nilai = 0


    def dandy(self):
        if self.quest == "M":
            print("_ _ _ _ _")
            self.isi = [int(x) for x in input("jawaban: ").split()]
            print("jawaban yang benar:", self.jaw)
            print("skor:", self.nilai)
        else:
            print("main aja sana, wleeeee")

    def malvin(self):
        import random

        x = [1, 2, 3, 4, 5]#angka
        v = ["a", "b", "C"]#huruf

        for i in range(len(x)):
            k = random.choice(x)
            self.jaw.append(k)
            x.remove(k)

    def skor(self):
        if self.jaw[0] == self.isi[0]:
            self.nilai += 20
        elif self.jaw[1] == self.isi[1]:
            self.nilai += 20
        elif self.jaw[2] == self.isi[2]:
            self.nilai += 20
        elif self.jaw[3] == self.isi[3]:
            self.nilai += 20
        elif self.jaw[4] == self.isi[4]:
            self.nilai += 20

def output():
    print("Selamat datang")
    q = ikan(input("ketik [M] jika sudah siap bermain:"))
    q.dandy()


if __name__ == "__main__":
    while True:
        output()

