from _common import *

page = dict(
    slug="suburbs-serviced", kind="hub", crumb="Service areas",
    title="Suburbs Serviced | Gold Coast, Logan & Southside | Moyle",
    description='All suburbs serviced by Moyle Plumbing & Gasfitting from Yatala: northern Gold Coast, Beenleigh, Logan, southside, Redlands. Call (07) 3807 7327.',
    h1="Suburbs serviced from our Yatala base",
    eyebrow="Service areas hub",
    intro="<p>Moyle Plumbing &amp; Gasfitting works out of 8 Belair Drive, Yatala, on the seam between the northern Gold Coast, Beenleigh and Logan. That places the growth corridor to the south, the established Logan suburbs to the north, Brisbane's southside beyond, and the acreage country to the east all within reach. Each area below has its own page with local detail.</p>",
    breadcrumb=[],
    body=sec("""
<h2>Northern Gold Coast</h2>
<p>The M1 corridor from Ormeau down to Helensvale: new estates, canal homes and a few older pockets.</p>
<ul class="link-grid">
<li>""" + L("plumber-ormeau", "Plumber Ormeau") + """</li>
<li>""" + L("blocked-drains-ormeau", "Blocked drains Ormeau") + """</li>
<li>""" + L("plumber-pimpama", "Plumber Pimpama") + """</li>
<li>""" + L("plumber-coomera", "Plumber Coomera") + """</li>
<li>""" + L("blocked-drains-coomera", "Blocked drains Coomera") + """</li>
<li>""" + L("plumber-hope-island", "Plumber Hope Island") + """</li>
<li>""" + L("plumber-helensvale", "Plumber Helensvale") + """</li>
<li>""" + L("emergency-plumbers-helensvale", "Emergency plumbers Helensvale") + """</li>
<li>""" + L("hot-water-gold-coast", "Hot water Gold Coast") + """</li>
<li>""" + L("plumbing-services-alberton", "Plumbing services Alberton") + """</li>
</ul>
<h2>Beenleigh and Logan</h2>
<p>Older homes, busy rental markets and commercial centres, from Beenleigh next door up to Springwood.</p>
<ul class="link-grid">
<li>""" + L("plumber-beenleigh", "Plumber Beenleigh") + """</li>
<li>""" + L("emergency-plumber-beenleigh", "Emergency plumber Beenleigh") + """</li>
<li>""" + L("plumber-loganholme", "Plumber Loganholme") + """</li>
<li>""" + L("plumber-shailer-park", "Plumber Shailer Park") + """</li>
<li>""" + L("hot-water-springwood", "Hot water Springwood") + """</li>
<li>""" + L("hot-water-system-logan", "Hot water system Logan") + """</li>
<li>""" + L("yarrabilba-plumber", "Yarrabilba plumber") + """</li>
</ul>
<h2>Brisbane southside</h2>
<p>Established brick homes and townhouse complexes, grouped into southside runs.</p>
<ul class="link-grid">
<li>""" + L("plumber-eight-mile-plains", "Plumber Eight Mile Plains") + """</li>
<li>""" + L("plumber-rochedale-south", "Plumber Rochedale South") + """</li>
<li>""" + L("hot-water-repairs-brisbane-southside", "Southside hot water repairs") + """</li>
<li>""" + L("hot-water-systems-brisbane-southside", "Southside hot water systems") + """</li>
</ul>
<h2>Redlands and acreage</h2>
<p>Tank water, pumps and septic country to the east.</p>
<ul class="link-grid">
<li>""" + L("plumber-mount-cotton", "Plumber Mount Cotton") + """</li>
<li>""" + L("plumber-redland-bay", "Plumber Redland Bay") + """</li>
</ul>
""") + soft("""
<h2>Not listed?</h2>
<p>The pages above are the suburbs we attend most, not a fence. Stapylton, Eagleby, Upper Coomera, Paradise Point, Cornubia, Daisy Hill, Underwood, Logan Village and Jimboomba are all regular stops. Ring """ + PHONE + """ with your suburb and the job for a straight answer on whether we cover it.</p>
<h2>How distance affects the visit</h2>
<p>Suburbs next to Yatala, such as Ormeau, Beenleigh and Alberton, are easy to fit in at short notice. The Gold Coast corridor is a direct run down the M1. Southside and Redlands jobs are grouped into runs so travel does not inflate the price. For an urgent fault anywhere in the area, the """ + H("urgent callout home page") + """ page sets out what to isolate while a plumber is on the way. The full list of what we do in every suburb is on the """ + L("all-services-available", "services page") + """. Moyle Plumbing has served this patch since 1983; the wider story is on the """ + M("the business's main website") + """ site.</p>
"""),
    faqs=[
        ("Do you charge travel for suburbs further from Yatala?",
         "<p>Give us the suburb and the job over the phone and the charges are settled before dispatch. Grouping southside and Redlands work into runs keeps travel from adding to the cost.</p>"),
        ("Which suburbs get the fastest emergency response?",
         "<p>The ones closest to the depot: Ormeau, Beenleigh, Alberton, Stapylton and Pimpama, followed by the rest of the M1 corridor. We always tell you a realistic time rather than a hopeful one.</p>"),
        ("Do you cover the southern Gold Coast?",
         "<p>Our regular area ends around Helensvale and Hope Island. For anything further south, ring and ask; we will say honestly whether it makes sense for us to attend.</p>"),
    ],
    related=[
        ("all-services-available", "All services"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("contact-us", "Contact"),
        ("about-us", "About us"),
    ],
)
