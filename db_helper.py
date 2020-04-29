from app.models import Books
from app import db

book1 = Books(
	name_ml="കറപ്പൻ",
	name_en="KARAPPAN",
	type_of_book="Novel",
	synopsis="സാമൂഹിക കേരളത്തിന്റെ പരിവര്‍ത്തനത്തില്‍ മുഖ്യമായ പങ്കുവഹിച്ച \
			രണ്ട് സംഭവങ്ങളാണ് നവോത്ഥാന കാലഘട്ടവും കമ്മ്യൂണിസ്റ്റ് \
			പ്രസ്ഥാനത്തിന്റെ ഉദയവും. ഇവ രണ്ടിലും നിസ്വാര്‍ത്ഥവും \
			ചെറുതല്ലാത്തതുമായ പങ്കുവഹിക്കുകയും എന്നാല്‍ ചരിത്രത്തിന്റെ \
			യവനികയ്ക്കു പിന്നില്‍ വിസ്മൃതരായി മറയുകയും ചെയ്ത നിരവധിപേര്‍ \
			ഇന്നും ഇടറി ജീവിക്കുന്നുണ്ട്്. നമ്മുടെ പ്രാണനെ പ്രചോദിപ്പിക്കുന്ന \
			ചില അംശങ്ങളെങ്കിലും അവര്‍ നമ്മുടെ ഓര്‍മ്മകളില്‍ \
			അവശേഷിപ്പിച്ചുപോയിട്ടുണ്ട്. അത്തരം നിസ്വാര്‍ത്ഥരില്‍ ഒരാളാണ് കറപ്പന്‍ \
			എന്ന ദലിതന്‍. അതിന്റെ ഓര്‍മ്മപ്പെടുത്തലും വീണ്ടെടുപ്പുമാണ് ഈ \
			നോവല്‍",
	publisher="DC BOOKS",
	publication_date="02-09-13",
	languge="Malayalam",
	isbn="9788126442959",
	web_link="https://dcbookstore.com/books/karappan")

book2 = Books(
	name_ml="പുളിനെല്ലി സ്റ്റേഷൻ",
	name_en="PULINELLI STATION",
	type_of_book="Short Stories",
	synopsis="രചനാകൗശലവും രൂപഭദ്രതയുമല്ല ജീവിതത്തിന്റെ സത്യമാണ് \
			പ്രധാനമെന്നു തെളിയിക്കുന്ന കഥകള്‍. അനുഭവതീക്ഷ്ണമായ ജീവിതത്തിന്റെ \
			വൈകാരികാംശങ്ങളെ സ്വാംശീകരിച്ചുകൊണ്ടുള്ള എഴുത്ത്. \
			ആനുകാലികങ്ങളില്‍ പ്രസിദ്ധീകരിച്ചുവന്നപ്പോള്‍ത്തന്നെ ഏറെ \
			ചര്‍ച്ചചെയ്യപ്പെട്ടതാണ് ഈ കഥകളെല്ലാം. അര്‍ജന്റീന ഫാന്‍സ് \
			കാട്ടൂര്‍ക്കടവ്, മൊയ്തു പടിയത്ത്, പുളിനെല്ലി സ്റ്റേഷന്‍, പതിനഞ്ചു \
			വര്‍ഷങ്ങള്‍ക്കുശേഷം, കിഴക്കേ ചെറൂക്കിലെ നാരായണിയമ്മ, \
			യുദ്ധാനന്തരവംശങ്ങള്‍ തുടങ്ങി പതിന്നാലു കഥകള്‍",
	publisher="DC BOOKS",
	publication_date="15-01-2020",
	languge="Malayalam",
	isbn="9789353902278",
	web_link="[https://dcbookstore.com/books/pulinelli-station,\
			https://www.amazon.in/PULINELLI-STATION-ASHOKAN-CHARUVIL/dp/9353902274/]")

book3 = Books(
	name_ml="തിരഞ്ഞെടുത്ത കഥകൾ",
	name_en="THIRANJEDUTHA KATHAKAL (ASOKAN CHARUVIL)",
	type_of_book="Short Stories",
	synopsis="ജീവിതത്തിന്റെ പ്രത്യക്ഷ യഥാര്‍ത്ഥ്യങ്ങളെയും സാമൂഹിക \
			വൈരുധ്യങ്ങളെയും കഥാവിഷയമാക്കുമ്പോള്‍ത്തന്നെ, അതിനുമപ്പുറത്ത് \
			ജീവിതത്തിന്റെ അപരപാഠങ്ങളെയും ആഖ്യാനം ചെയ്യാനും വ്യാഖ്യാനിക്കാനും \
			ഈ രചനകള്‍ക്കാവുന്നു. ഭാവാത്മകതയും സംവേദനീയതയും പുലര്‍ത്തുന്ന \
			നിബ്ദ്ധമായ പുതുമകള്‍ നിഗൂഹനം ചെയ്യുന്ന ഭാഷാശില്പത്തിലൂടെ അത് \
			നിരന്തരം സൂക്ഷ്മമായ നവീകരണത്തിന് സ്വയം സജ്ജമാകുന്നു. ഇങ്ങനെ \
			മലയാള ചെറുകഥയുടെ സമകാലിക മുഖത്തിന്റെ ഭക്തപ്രസാദമായി അശോകന്‍ \
			ചരുവിലിന്റെ ചെറുകഥകള്‍ മാറുന്നു.-ഡോ. കെ. എസ്. രവികുമാര്‍",
	publisher="DC BOOKS",
	publication_date="21-04-14",
	languge="Malayalam",
	isbn="9788126432233",
	web_link="https://dcbookstore.com/books/thiranjedutha-kathakal-asokan-charuvil")

book4 = Books(
	name_ml="കൽപ്പനിക്കാരൻ",
	name_en="KALPPANIKKARAN",
	type_of_book="Short Stories",
	synopsis="മനുഷ്യനായിരിക്കുക എന്നതാണ് മനുഷ്യജീവിതത്തിന്റെ \
			നിതാന്തസത്യമെന്നും അതുപേക്ഷ ിച്ചുകൊണ്ടുള്ള മാനവികത വെറും \
			യാന്ത്രികാനുഭവങ്ങളുടെ ആവർത്തനവിധി മാത്രമായിരിക്ക ുമെന്നും \
			ഉദ്‌ഘോഷിക്കുന്ന കഥകൾ. ആത്മകഥയ്‌ക്കൊരാമുഖം, നോക്കുകൂലി, \
			കാട്ടൂർ ക്കടവിലെ കൽപ്പണിക്കാരൻ, മദ്യവിമുക്തമായ പുളിക്കടവ് \
			തുടങ്ങി സമീപകാലത്ത് ചർച്ച ചെയ്യപ്പെട്ട എട്ടു കഥകൾ.",
	publisher="DC BOOKS",
	publication_date="23-11-16",
	languge="Malayalam",
	isbn="9788126474387",
	web_link="https://dcbookstore.com/books/kalppanikkaran")

book5 = Books(
	name_ml="ദൈവം കഥ വായിക്കുന്നുണ്ട്",
	name_en="DAIVAM KATHA VAYIKKUNNUNDU",
	type_of_book="Memoirs",
	synopsis="അനുഭവക്കുറിപ്പുകൾ എന്ന ഭാവേന ഈ പുസ്തകം ഞാൻ എഴുതിയിട്ട് ഒരു \
			വർഷം പിന്നിട്ടു. ഇതിനു മുമ്പ് ജീവിതത്തിലെ മറ്റൊരു ഘട്ടത്തെക്കുറിച്ച് \
			ഞാൻ എഴുതിയിട്ടുണ്ട്. അതു പുസ്തകരൂപത്തിൽ പുറത്തു വന്നു---'ചിമ്മിനി \
			വെളിച്ചത്തിൽ പ്രകാശിക്കുന്ന ലോകം.' ഒരു നിസ്സാര മനുഷ്യൻ \
			അഹങ്കാരത്തോടെ നിവർന്നു നിന്ന് 'ഞാൻ' എന്നു പറയുകയാണ്. അങ്ങനെ \
			ചെയ്യാൻ പാടുണ്ടോ എന്നു ചോദിക്കാം. ഒരാൾ കുറെക്കാലം ഭൂമിയിൽ \
			ജീവിച്ചു. കുറെ വികൃതികളും വേദനകളും ആഹ്‌ളാദങ്ങളുമായി \
			കുട്ടിക്കാലംപിന്നിട്ടു. വയൽവരമ്പിലൂടെ നടന്നു. പൂക്കളെയും കിളികളെയും \
			നോക്കിനിന്നു. കുളിച്ചു. ഭക്ഷണം കഴിച്ചു. ആപ്പീസിൽ പോയി ജോലി \
			ചെയ്തു. ചെയ്യാതിരുന്നു. തരപ്പെട്ടപ്പോൾ കൈക്കൂലി വാങ്ങിച്ചു. \
			അഥവാ വാങ്ങിച്ചില്ല. ഇതിനൊക്കെ എന്തു പ്രസക്തി എന്നു ചോദിക്കാം. \
			നിങ്ങൾ ജനിച്ചു, ജീവിച്ചു, മരിച്ചു. ശരി. പക്ഷേ, ചെയ്ത അതിശയ \
			പ്രവൃത്തി എന്ത്?",
	publisher="DC BOOKS",
	publication_date="01-03-13",
	languge="Malayalam",
	isbn="9788126440634",
	web_link="https://dcbookstore.com/books/daivam-katha-vayikkunnundu")

book6 = Books(
	name_ml="ചിമ്മിണിവെളിച്ചത്തിൽ പ്രകാശിക്കുന്ന ലോകം",
	name_en="CHIMMINIVELICHATHIL PRAKASIKUNNA LOKAM",
	type_of_book="Short Stories",
	synopsis="",
	publisher="CURRENT BOOKS",
	publication_date="01-06-15",
	languge="Malayalam",
	isbn="9788120000000",
	web_link="https://dcbookstore.com/books/chimminivelichathil-prakasikunna-lokam")

book7 = Books(
	name_ml="കങ്കാരുനൃത്തം",
	name_en="KANGARUNRUTHAM",
	type_of_book="Novel",
	synopsis="",
	publisher="DC BOOKS",
	publication_date="01-01-1970",
	languge="Malayalam",
	isbn="9788126411313",
	web_link="[https://dcbookstore.com/books/kangarunrutham,\
			https://www.amazon.in/Kangarunrutham-Asokan-Charuvil/dp/8126411317]")

book8 = Books(
	name_ml="നോവെല്ലകൾ",
	name_en="Novellakal Ashokan Charuvil",
	type_of_book="Novella",
	synopsis="",
	publisher="CHINTHA PUBLISHERS",
	publication_date="01-01-1970",
	languge="Malayalam",
	isbn="9789383903146",
	web_link="https://dcbookstore.com/books/kangarunrutham")

book9 = Books(
	name_ml="എഴുത്തിൻറെ വെയിലും നിലാവും",
	name_en="Ezhuthinte Veyilum Nilavum",
	type_of_book="",
	synopsis="",
	publisher="Progress Publishers",
	publication_date="",
	languge="Malayalam",
	isbn="9788192832616",
	web_link="[https://www.amazon.in/Ezhuthinte-Veyilum-Nilavum-Ashokan-Charuvil/dp/8192832619/]")

book10 = Books(
	name_ml="കഥയുടെ മറുകര",
	name_en="KADHAYUDE MARUKARA",
	type_of_book="",
	synopsis="",
	publisher="CHINTHA PUBLISHERS",
	publication_date="",
	languge="Malayalam",
	isbn="9789382167631",
	web_link="[https://www.amazon.in/KADHAYUDE-MARUKARA-ASHOKAN-CHARUVIL/dp/9382167633]")

book11 = Books(
	name_ml="മറവിയിൽ മറഞ്ഞത് മനുഷ്യൻ",
	name_en="Maraviyil maranjathu manushyan",
	type_of_book="Memoirs",
	synopsis="മലയാളത്തിന്റെ പ്രിയ കഥാകാരന്‍ അശോകന്‍ ചരുവിലിന്റെ \
			ഓര്‍മ്മക്കുറിപ്പുകള്‍, പ്രതിഷേധങ്ങള്‍, പ്രതികരണങ്ങള്‍ സമകാലിക \
			സംവാദങ്ങളിലെ ധീരമായ ഇടപെടലുകള്‍, അനുഭവങ്ങളുടെ അടയാളങ്ങള്‍ \
			പതിഞ്ഞുകിടക്കുന്ന കുറിപ്പുകള്‍ എന്നിങ്ങനെ ഒരെഴുത്തുകാരന്റെ \
			വിചാരങ്ങളുടെയും വികാരങ്ങളുടെയും ലോകമാണ് ഈ പുസ്തകത്തില്‍.",
	publisher="CHINTHA PUBLISHERS",
	publication_date="",
	languge="Malayalam",
	isbn="978-9387842618",
	web_link="[https://www.amazon.in/Maraviyil-maranjathu-manushyan-Ashokan-Charuvil/dp/9387842614/]")

book12 = Books(
	name_ml="കാട്ടൂർക്കടവിലെ ക്രൂരകൃത്യം",
	name_en="Kattorkadavile Krooakruthyam",
	type_of_book="",
	synopsis="",
	publisher="Current Books Thrissur",
	publication_date="",
	languge="Malayalam",
	isbn="",
	web_link="[https://www.amazon.in/Kattorkadavile-Krooakruthyam-Ashokan-Charuvil/dp/8122606970/]")

book13 = Books(
	name_ml="അന്തിക്കാട് എത്ര ജെന്നിമാർ ഉണ്ട്",
	name_en="Anthikkadu Ethra Jennimar Undu?",
	type_of_book="",
	synopsis="",
	publisher="Nirmala Books",
	publication_date="",
	languge="Malayalam",
	isbn="",
	web_link="[https://www.amazon.in/Anthikkadu-Ethra-Jennimar-Ashokan-Charuvil/dp/B007E4XGBK/]")

db.session.add(book1)
db.session.commit()
