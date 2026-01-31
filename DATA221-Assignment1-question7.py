def convertSeconds(seconds):
    if seconds < 0 or seconds >= 86400:
        return "Invalid input"

    hoursSinceMidnight = seconds // 3600
    minutesSinceMidnight = (seconds % 3600) // 60
    secondsSinceMidnight = seconds % 60

    if hoursSinceMidnight < 12:
        timeIndicator = "AM"
    else:
        timeIndicator = "PM"

    hoursSinceMidnight = hoursSinceMidnight % 12
    if hoursSinceMidnight == 0:
        hoursSinceMidnight = 12

    return f" {hoursSinceMidnight} {minutesSinceMidnight} {secondsSinceMidnight} {timeIndicator}"

