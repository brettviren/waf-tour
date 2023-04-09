def configure(cfg):
    cfg.load("org", tooldir='.')
    html = cfg.path.find_resource("html.el")

    # Want a customized export.
    cfg.env.EMACSFLAGS_HTML = [
        '--load',html.abspath(),
        '--eval','''(progn
                      (outline-show-all)
                      (font-lock-flush)
                      (font-lock-fontify-buffer)
                      (org-html-export-to-html))''']

def build(bld):
    bld.load("org", tooldir='.')
    org = bld.path.find_resource("README.org")
    pdf = org.parent.make_node("waf-tour.pdf")
    html = org.parent.make_node("index.html")
    print(org,pdf,html)
    bld(features="org2pdf", source=org, target=pdf)
    bld(features="org2html", source=org, target=html)
    
    
