from _common import *

page = dict(
    slug="about-us", kind="core", crumb="About us",
    title="About Moyle Plumbing & Gasfitting | Family Owned Since 1983",
    description="Moyle Plumbing & Gasfitting: a family owned Yatala plumbing and gas business trading since 1983, licensed, insured and priced upfront. Call (07) 3807 7327.",
    h1="About Moyle Plumbing &amp; Gasfitting",
    eyebrow="Family owned since 1983",
    intro="<p>Moyle Plumbing &amp; Gasfitting is a family owned and operated plumbing and gasfitting business that has traded from the northern Gold Coast since 1983. It is based at Yatala and works across the northern Gold Coast, Beenleigh, Logan and Brisbane's southside, for homeowners, property managers and businesses.</p>",
    breadcrumb=[],
    body=sec("""
<h2>What the business stands on</h2>
<ul class="cards cols-2">
<li class="card"><h3>Licensed and insured</h3><p>QBCC licence 1077154 covers the plumbing and gas work. Insurance is in place, and certificates can be supplied for contractor files. Gas work is done by licensed gasfitters and certified.</p></li>
<li class="card"><h3>Upfront, set pricing</h3><p>Diagnosis first, then a fixed figure for the repair before anything is touched. Any change is costed before it happens, and a no costs you nothing.</p></li>
<li class="card"><h3>Fast response</h3><p>When it is truly urgent, the goal is to be there that day. Ringing gets you an honest view of the day, never an empty promise.</p></li>
<li class="card"><h3>Clean and tidy</h3><p>Drop sheets, boot covers and a clean-up before leaving. The work area is left the way it was found, or better.</p></li>
</ul>
""") + soft("""
<h2>The work</h2>
<p>Four decades of trade work on the same patch has covered just about everything a house, a shop or a rental can throw up:</p>
<ul class="checks">
<li>Domestic maintenance and repairs, from dripping taps to repiping a house.</li>
<li>Emergency callouts for burst pipes, blocked sewers, failed hot water and gas leaks.</li>
<li>Commercial work for retail, hospitality, workshops, schools and unit complexes.</li>
<li>Real estate and property manager work across a large rental market.</li>
<li>Blocked drains, hot water, concealed leak detection, gas fitting, toilets, pumps and renovations.</li>
</ul>
<p>Every service is listed on the """ + L("all-services-available", "services page") + """, with the areas we cover on the """ + L("suburbs-serviced", "suburbs page") + """.</p>
""") + sec("""
<h2>Why local matters</h2>
<p>Working from Yatala instead of a depot across town means the tradesperson who arrives has already seen the estates, the old streets, the canal soils and the acreage, and has worked on the same kinds of houses many times before. It also means shorter travel on an urgent job. The """ + H("emergency plumbing home page") + """ explains how that works from the first call.</p>
<h2>Where to find us</h2>
<p>Moyle Plumbing &amp; Gasfitting, 8 Belair Drive, Yatala QLD 4207. Ring """ + PHONE + """ or email """ + MAILTO + """. The crew is normally out on the road, so phone ahead of any visit. Contact details and a map are on the """ + L("contact-us", "contact page") + """. Advice articles from the trade are collected under """ + L("handy-hints-blog", "handy hints") + """, and the business's main website is """ + M("Moyle Plumbing &amp; Gasfitting") + """.</p>
"""),
    faqs=[
        ("How long has Moyle Plumbing been operating?",
         "<p>The business has been trading since 1983 and remains family owned and operated.</p>"),
        ("What is your licence number?",
         "<p>QBCC licence 1077154. The ABN is 77 105 255 534. Both appear in the footer of every page on this site.</p>"),
        ("Do you employ subcontractors?",
         "<p>Plumbing and gas work is done by the business's own licensed tradespeople. Where a job needs another trade, such as an electrician for a hot water connection or a waterproofer on a renovation, we coordinate it and tell you who is doing what.</p>"),
    ],
    related=[
        ("all-services-available", "All services"),
        ("suburbs-serviced", "Suburbs serviced"),
        ("contact-us", "Contact"),
        ("environmental-green-plumbers", "Green plumbing"),
        ("products-and-brands", "Products and brands"),
    ],
)
