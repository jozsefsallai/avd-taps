from core import AVDTaps

def main():
    try:
        taps = AVDTaps()
        taps.run()
    except KeyboardInterrupt:
        print('Goodbye!')

if __name__ == '__main__':
    main()
