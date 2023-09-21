package main

func main() {
	generateURL('https://rokna.net/', 'feeds')
}

func generateURL(uri, path string) string {
	return uri + path
}

func bootRequest(method, url string) {
	switch method {
		case "get":
			println("get")
			break
		case "post":
			println("post")
			break
	}
}
