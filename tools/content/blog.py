from _common import *

page = dict(
    slug="blog", kind="hub", crumb="Articles",
    title="Plumbing Articles & Guides | Moyle Plumbing & Gasfitting",
    description="Plumbing articles and guides by topic from Moyle Plumbing & Gasfitting, Yatala: emergencies, common questions and pipe failures. Call (07) 3807 7327.",
    h1="Plumbing articles and guides by topic",
    eyebrow="Articles index",
    intro="<p>Plumbing articles and guides from Moyle Plumbing &amp; Gasfitting, sorted by the problem they help with rather than by date. The pieces are the same ones collected under handy hints, arranged here so you can jump straight to the topic that matches what is going on at your place.</p>",
    breadcrumb=[],
    body=sec("""
<h2>Something is wrong right now</h2>
<ul>
<li>""" + L("helpful-tips-for-plumbing-emergencies", "Helpful tips for plumbing emergencies") + """: shutting off water, gas and the heater, and how to hold the fort until help comes.</li>
<li>Service page: """ + L("emergency-plumbing", "emergency plumbing") + """.</li>
</ul>
<h2>Getting a straight answer</h2>
<ul>
<li>""" + L("frequently-asked-questions", "Frequently asked plumbing questions") + """: pricing, pressure, wipes, hot water life, gas rules and more, answered briefly.</li>
<li>Service pages: """ + L("general-plumbing-maintenance", "plumbing maintenance") + """ and """ + L("all-services-available", "all services") + """.</li>
</ul>
<h2>Pipes and leaks</h2>
<ul>
<li>""" + L("electrolysis-in-copper-pipe", "Electrolysis in copper pipe") + """: how copper fails from within and how we confirm it.</li>
<li>Service pages: """ + L("leak-repairs", "leak detection") + """ and """ + L("burst-pipe", "burst pipe repair") + """.</li>
</ul>
""") + soft("""
<h2>About these guides</h2>
<p>Everything here is written from the trade's side of the job by a family business that has worked the northern Gold Coast, Beenleigh and Logan since 1983. The aim is to help you decide what to do next, whether that is a quick fix, a booked visit or a visit to the """ + H("emergency plumber near you") + """ page. Gas is the one area where the only advice is to isolate and call a licensed gasfitter. The chronological list of the same articles is on the """ + L("handy-hints-blog", "handy hints page") + """, and the business's own site is """ + M("www.moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Reading order for a new homeowner</h2>
<p>If you have just moved into a house on the northern Gold Coast, start with the emergency tips and go and find your water meter today. Then read the questions article for the pressure and hot water sections, because high mains pressure and an ageing heater are the two things most likely to cost you money in the first year. The copper article matters most if the house is older than the 1990s. Between them they cover the calls we take most often, and each ends with the number to ring when reading is no longer enough.</p>
<h2>Sharing and reuse</h2>
<p>Property managers and body corporate committees are welcome to link to any of these pages from their own tenant or owner information. The advice applies to any Queensland home, though the licensing and compliance details are specific to this state.</p>
"""),
    faqs=[
        ("How often are new articles added?",
         "<p>When a question comes up often enough on the phone to be worth writing down properly. There is no fixed schedule.</p>"),
        ("Can I share these guides with tenants?",
         "<p>Yes. Property managers are welcome to send the emergency tips article to tenants so they know how to isolate water and gas before a plumber arrives.</p>"),
        ("Are the articles a substitute for calling a plumber?",
         "<p>They help you understand and contain a problem. Repairs, and anything involving gas, still need a licensed tradesperson.</p>"),
    ],
    related=[
        ("handy-hints-blog", "Handy hints"),
        ("helpful-tips-for-plumbing-emergencies", "Emergency tips"),
        ("frequently-asked-questions", "Plumbing FAQs"),
        ("electrolysis-in-copper-pipe", "Electrolysis in copper pipe"),
    ],
)
