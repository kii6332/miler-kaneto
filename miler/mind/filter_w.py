import re
def filter_w(wd):
	fil = re.sub(r'\b(fuck|shit|bitch|asshole|bastard|dick|pussy|cunt|nigger|faggot|slut|whore|retard|damn|crap|cock|jerk|twat|suck|rape|suicide|freak|idiot|moron|stupid|kys|nazi|hitler|porn|sex|boobs|penis|vagina|nude|nudes|xxx|hentai|incest|horny)\b','[**bad word**]', wd , flags=re.IGNORECASE)
	wd = re.sub(r'(https://|http://)\S+','[**link**]', wd , flags=re.IGNORECASE)
	return fil
