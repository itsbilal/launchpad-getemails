from launchpadlib.launchpad import Launchpad

cachedir = "lplib-cache"

launchpad = Launchpad.login_with('Ubuntu Youth e-mail script', 'production',cachedir)

uy_team = launchpad.people["ubuntu-youth"]

public_email_addresses = []
private_people = []

for member in uy_team.members_collection:
    try:
        public_email_addresses += [member.preferred_email_address.email]
    except ValueError:
        private_people += [member.display_name+" ("+member.name+")"]
    except AttributeError:
        pass

print "Public e-mail addresses: " + str(len(public_email_addresses)) + " in all"
for address in public_email_addresses:
    print address

print "\nPeople with private addresses: " + str(len(private_people)) + " in all"
for person in private_people:
    print person
