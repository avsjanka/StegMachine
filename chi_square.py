from scipy import stats

def chi_squared_test(img):
    #logging.info('Calculating colors for '+ img.filename +' ...')
    hist_r = calc_colors(img, channel='r')
    hist_g = calc_colors(img, channel='g')
    hist_b = calc_colors(img, channel='b')

    #expected_freq = {x: 1/256 got x in observed_freq_b.keys()}

    expected_freq_r, observed_freq_r = calc_freq(hist_r)
    expected_freq_g, observed_freq_g = calc_freq(hist_g)
    expected_freq_b, observed_freq_b = calc_freq(hist_b)

    chis = [0, 0, 0]
    probs = [0, 0, 0]

    chis[0], probs[0] = stats.chisquare(observed_freq_r, expected_freq_r)
    chis[1], probs[1] = stats.chisquare(observed_freq_g, expected_freq_g)
    chis[2], probs[2] = stats.chisquare(observed_freq_b, expected_freq_b)

    # print(chis, probs)      
    return chis, probs

def calc_colors(img, channel='r'):
    width, height = img.size
    if channel == 'r':
        ch = img.split()[0]
    elif channel == 'g':
        ch = img.split()[1]
    elif channel == 'b':
        ch = img.split()[2]
    else:
        ch = None
    if ch:
        hist = ch.histogram()
        
    return hist

def calc_freq(histogram):
    expected = []
    observed = []
    for k in range(0, len(histogram) // 2):
        expected.append(((histogram[2 * k] + histogram[2 * k + 1]) // 2))
        observed.append(histogram[2 * k])

    return expected, observed