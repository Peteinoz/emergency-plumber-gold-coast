from _common import *

page = dict(
    slug="handy-hints-blog", kind="hub", crumb="Handy hints",
    title="Handy Plumbing Hints | Moyle Plumbing & Gasfitting",
    description='Handy plumbing hints from a licensed Gold Coast trade: emergency steps, common questions answered, and why copper pipes fail. Call (07) 3807 7327.',
    h1="Handy plumbing hints from the trade",
    eyebrow="Handy hints",
    intro="<p>Handy plumbing hints written by the people who see the results of getting it wrong. These articles cover what to do when something goes wrong, the questions we are asked most, and a few of the odd failures we find in northern Gold Coast homes. Practical, specific and free of sales talk.</p>",
    breadcrumb=[],
    body=sec("""
<h2>Articles</h2>
<ul class="cards post-list">
<li class="card"><h3>""" + L("helpful-tips-for-plumbing-emergencies", "Helpful tips for plumbing emergencies") + """</h3><p>Where the water meter, gas valve and hot water breaker are, how to shut each one, and the mistakes to avoid while help is coming.</p></li>
<li class="card"><h3>""" + L("frequently-asked-questions", "Frequently asked plumbing questions") + """</h3><p>Short answers to the things people ask us on the phone every week: pricing, pressure, wipes, dripping taps, hot water and gas.</p></li>
<li class="card"><h3>""" + L("electrolysis-in-copper-pipe", "Electrolysis in copper pipe") + """</h3><p>Pinholes in copper: the causes, the signs and the remedies.</p></li>
</ul>
""") + soft("""
<h2>How to use these hints</h2>
<p>Each article is written for a homeowner standing in a wet kitchen, not for another plumber. The emergency article is worth reading before you need it, so you know where the meter is. The questions article helps you judge whether something can wait for a booking. The copper article explains one of the more puzzling leaks we see in older homes across Beenleigh, Loganholme and Helensvale.</p>
<p>None of this replaces a licensed plumber for the actual repair, and none of it involves gas work, which must never be attempted by anyone unlicensed. When the problem is happening now, the """ + H("urgent plumber Gold Coast page") + """ has the shut-off steps and the phone number. The """ + L("blog", "articles index") + """ lists the same pieces by topic. The services behind these articles are on the """ + L("all-services-available", "services page") + """, and the business is at """ + M("moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>What the articles do not cover</h2>
<p>Deliberately, nothing here shows you how to open a gas fitting, replace a hot water valve or cut into a water main. Those jobs are licensed work in Queensland for good reasons, and the articles stop at the point where a homeowner should hand over. What they do cover in detail is everything up to that point: recognising the fault, making it safe, limiting the damage and describing it clearly on the phone, which is where most of the time and money in an emergency is saved.</p>
"""),
    faqs=[
        ("Can I suggest a topic?",
         "<p>Yes. Email admin@moyleplumbing.com.au with the question and, if it comes up often, it may become an article.</p>"),
        ("Is the advice specific to Queensland?",
         "<p>Yes. Licensing rules, water efficiency requirements and the housing types described are all Queensland and Gold Coast specific.</p>"),
        ("Do the articles cover gas?",
         "<p>Only what to do if you smell it: isolate, ventilate, get outside and call. Gas work is never a do-it-yourself job.</p>"),
    ],
    related=[
        ("helpful-tips-for-plumbing-emergencies", "Emergency tips"),
        ("frequently-asked-questions", "Plumbing FAQs"),
        ("electrolysis-in-copper-pipe", "Electrolysis in copper pipe"),
        ("blog", "Articles index"),
        ("emergency-plumbing", "Emergency plumbing"),
    ],
)
