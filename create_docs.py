import os, json, shutil


if __name__ == "__main__":
	
	data = None
	with open("links.json", "r") as f:
		data = json.load(f)
		
	if not data:
		exit()
	
	archive = ""
	latest_url = ""	
	latest_date = ""
	latest_id = ""
	
	latest_url = data["links"][-1]["url"]
	latest_date = data["links"][-1]["date"]
	latest_id = latest_url[latest_url.rindex("?v=")+3:]
	
	for item in data["links"]:
		archive += "<p><a href='"+item["url"]+"' style='color: #484848;'>"+item["date"]+"</a></p>"
		
	if latest_url == "":
		exit()
		
	if os.path.isdir("./docs"):
		shutil.rmtree("./docs")
	os.mkdir("./docs")
	
	shutil.copytree("res", "docs/res")
	shutil.copy("index.html", "docs/index.html")
	shutil.copy("archive.html", "docs/archive.html")
	shutil.copy("impressum.html", "docs/impressum.html")
	
	for f in os.listdir("docs/res"):
		if f.endswith(".psd"):
			os.remove("docs/res/"+f)
			
	for name in ("index", "archive", "impressum"):
		html = ""
		with open("docs/"+name+".html", "r") as f:
			html = f.read()
			
		html = html.replace("LATEST_URL", latest_url)
		html = html.replace("LATEST_EMBED", "https://www.youtube.com/embed/"+latest_id+"/")
		html = html.replace("LATEST_DATE", latest_date)
		html = html.replace("LIST_HERE", archive)
		
		html = html.replace("SLASH_LATEST", latest_url)
		html = html.replace("SLASH_ARCHIVE", "archive.html")
		html = html.replace("SLASH_IMPRESSUM", "impressum.html")
		html = html.replace("ORIGINAL_URL", "index.html")
		
		with open("docs/"+name+".html", "w") as f:
			f.write(html)
