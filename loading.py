import sys

def progress_bar(current, total, prefix=''):
    
    len = 20
    
    filled_width = int(round(len * current / total))
    percentage = round(100.0 * current / total, 1)
    bar = '⬜' * filled_width + '⬛' * (len - filled_width)

    sys.stdout.write(f'\r{prefix} |{bar}| {percentage}%')
    sys.stdout.flush()

    if current == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

# Test progress_bar
if __name__ == '__main__':
    import time
    
    for i in range(100):
        progress_bar(i + 1, 100, prefix=f'Progress: {i + 1} / 100')
        time.sleep(0.1)