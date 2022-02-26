def alpha(sample):
    if sample.isalpha():
        return "isalpha"
    elif sample.isdigit():
        return "isdigit"
    elif sample.isalnum():
        return "isalnum"
alpha("289sf")