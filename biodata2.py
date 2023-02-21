def get_biodata():
    kebutuhan_data = ['nama', 'alamat', 'ttl', 'pekerjaan', 'status']
    inputan_biodata = []
    for data in kebutuhan_data:
        inputan = input('input {}: '.format(data))
        inputan_biodata.append(inputan)

    print('================================')
    print('Biodata anda adalah: ')

    for id, hasil in enumerate(inputan_biodata):
        print(kebutuhan_data[id] + ': ' + hasil)


def run():
    while True:
        get_biodata()
        input_lagi = input('apakah input lagi? (y/n): ')
        if input_lagi == 'y':
            continue
        elif input_lagi == 'n':
            break


if __name__ == '__main__':
    run()