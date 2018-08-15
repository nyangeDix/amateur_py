class Voting():

    def get_voter_name(self, name):
        return name

    def get_age(self, yob):
        current_year = 2018
        age = current_year - yob
        return age

    def authority(self, yob):
        function_age = self.get_age(yob)
        if function_age >= 18:
            status_report = "Allowed to vote"
        elif function_age <= 18:
            status_report = "Not allowed to vote"
        return status_report

Voting_day = Voting()
name_voter = input("Please enter your name: ")
v1_name = Voting_day.get_voter_name(name_voter)
print("Voter's name: " + v1_name)

yob = input("Enter Year of birth: ")
v1_get_status = Voting_day.authority(int(yob))
print ("Voter status: " + v1_get_status)  