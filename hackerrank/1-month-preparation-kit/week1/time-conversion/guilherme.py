def timeConversion(s):
    # Write your code here
    am_pm = s[-2:]
    hour = s[0:2]
    minutes_seconds = s[2:-2]
    if am_pm == 'AM':
        if hour == '12':
            hour = '00'
    else:
        if hour != '12':
            hour = str(int(hour) + 12)

    return hour + minutes_seconds

assert timeConversion('12:01:00AM') == '00:01:00'
assert timeConversion('11:25:00AM') == '11:25:00'
assert timeConversion('12:00:11PM') == '12:00:11'
assert timeConversion('04:00:40PM') == '16:00:40'