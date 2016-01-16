#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


def preveriLasje(zapis):
    crna = "CCAGCAATCGC"
    rjava = "GCCAGTGCCG"
    korencek = "TTAGCTATCGC"
    if zapis.find(crna) != -1:
        return "crno barvo las"
    elif zapis.find(rjava) != -1:
        return "rjavo barvo las"
    elif zapis.find(korencek) != -1:
        return "oranzno barvo las"
    else:
        return "neznano barvo las"

def preveriObraz(zapis):
    kvadraten =  "GCCACGG"
    okrogel =  "ACCACAA"
    ovalen = "AGGCCTCA"
    if zapis.find(kvadraten) != -1:
        return "kvadratast obraz"
    elif zapis.find(okrogel) != -1:
        return "okrogel obraz"
    elif zapis.find(ovalen) != -1:
        return "ovalen obraz"
    else:
        return "neznano obliko obraza"


def preveriOci(zapis):
    modraOci = "TTGTGGTGGC"
    zelenaOci = "GGGAGGTGGC"
    rjavaOci = "AAGTAGTGAC"
    if zapis.find(modraOci) != -1:
        return "modre oci"
    elif zapis.find(zelenaOci) != -1:
        return "zelene oci"
    elif zapis.find(rjavaOci) != -1:
        return "rjave oci"
    else:
        return "neznano barvo oci"


def preveriSpol(zapis):
    moski = "TGCAGGAACTTC"
    zenska = "TGAAGGACCTTC"
    if zapis.find(moski) != -1:
        return "je moski"
    elif zapis.find(zenska) != -1:
        return "je zenska"
    else:
        return "je neznanega spola"


def preveriRaso(zapis):
    belec = "AAAACCTCA"
    crnec = "CGACTACAG"
    azijec = "CGCGGGCCG"
    if zapis.find(belec) != -1:
        return "je belec"
    elif zapis.find(crnec) != -1:
        return "je crnc"
    elif zapis.find(azijec) != -1:
        return "je azijec"
    else:
        return "je neznane rase"




class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        print "ertertert"
        return self.render_template("forenzika.html")
    def post(self):
        zapis = self.request.get("vnosnoPolje")
        zapis = zapis.strip(' ')
        barvaLas = preveriLasje(zapis)
        obraz = preveriObraz(zapis)
        oci = preveriOci(zapis)
        spol = preveriSpol(zapis)
        rasa = preveriRaso(zapis)

        oseba = "Oseba ima: " + barvaLas + ", " + obraz + ", " + oci + ", " + " ter " + spol + " in " + rasa
        print "test", oseba
        podatki = {"rezultat":oseba}
        return self.render_template("forenzika.html", podatki)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
