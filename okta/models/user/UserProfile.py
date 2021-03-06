class UserProfile:

    types = {
        'login': str,
        'email': str,
        'secondEmail': str,
        'firstName': str,
        'lastName': str,
        'displayName':str,
        'mobilePhone': str,
        'userType' : str,
        'manager': str,
        'startDate':str,
        'employeeNumber':str,
        'title':str,
        'department':str,
        'division':str,
        'streetAddress':str,
        'city':str,
        'state':str,
        'zipCode':str,
        'countryCode':str,
        'PHITrained':str
    }

    def __init__(self):

        self.login = None  # str
        self.email = None  # str
        self.secondEmail = None  # str
        self.firstName = None  # str
        self.lastName = None  # str
        self.displayName = None
        self.mobilePhone = None  # str
        self.userType = None
        self.manager = None
        self.startDate = None
        self.employeeNumber = None
        self.title = None
        self.department = None
        self.division = None
        self.streetAddress = None
        self.city = None
        self.state = None
        self.zipCode = None
        self.countryCode = None
        self.PHITrained = None
