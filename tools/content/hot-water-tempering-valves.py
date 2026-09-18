from _common import *

page = dict(
    slug="hot-water-tempering-valves", kind="service", crumb="Tempering valves",
    title="Tempering Valve Replacement Gold Coast | Moyle Plumbing",
    description="Tempering valve replacement and testing for hot water systems across the northern Gold Coast and Logan. Licensed, set pricing. Call (07) 3807 7327.",
    h1="Tempering valve replacement for hot water systems",
    eyebrow="Hot water safety",
    intro="<p>Tempering valve replacement is a small job that matters more than most people realise. The valve blends hot and cold so the water reaching your bathroom cannot scald, and when it fails you get water that is suddenly too hot, too cold or wildly variable. Moyle Plumbing &amp; Gasfitting tests and replaces them across the northern Gold Coast.</p>",
    breadcrumb=[("all-services-available", "Services"), ("hot-water", "Hot water")],
    service=dict(name="Tempering valve replacement", area="Gold Coast"),
    body=sec("""
<h2>What a tempering valve does</h2>
<p>Storage hot water is kept hot enough to control bacteria such as Legionella, which means the tank runs well above a safe skin temperature. The tempering valve sits on the outlet and mixes in cold water so the supply to baths, showers and basins is held at a safe temperature. Australian plumbing standards require one on the supply to bathrooms used for personal hygiene, and every new or replacement system installed in Queensland gets one.</p>
<p>Kitchen and laundry taps are often fed before the valve so dishes and washing get full-temperature water. That is why a kitchen tap can run much hotter than the bathroom.</p>
""") + soft("""
<h2>Signs the valve has failed</h2>
<ul class="checks">
<li>Shower temperature swings without anyone touching the tap.</li>
<li>Bathroom hot water is barely warm while the kitchen is scalding.</li>
<li>Hot water at the bathroom is suddenly much hotter than it used to be.</li>
<li>Hot water runs out far sooner than it did, becathe valve is passing too much cold.</li>
<li>The unit is more than a few years old and the valve has never been changed.</li>
</ul>
<p>Manufacturers generally recommend the valve be checked and replaced periodically rather than left until it fails, because a stuck valve can pass full-temperature water to a bathroom.</p>
""") + sec("""
<h2>What the job involves</h2>
<ol class="steps">
<li>Isolate the hot water unit and relieve the pressure.</li>
<li>Remove the old valve, check the strainers and the non-return valves on either side, and clean out any scale.</li>
<li>Fit the new valve with correct clearances so it can be serviced next time.</li>
<li>Restore supply and set the outlet temperature with a thermometer at the furthest bathroom tap, then record it.</li>
</ol>
<p>The whole job carries one price, given before we begin. If the real cause turns out to be a failed thermostat or a mixer letting cold across into the hot side, we tell you that instead of replacing a valve that was fine.</p>
<h2>Rentals and compliance</h2>
<p>Property managers ask us to check tempering valves as part of """ + L("water-compliancy", "water efficiency and compliance") + """ inspections and hot water servicing on rentals, since a scald in a tenanted property is a serious matter for the owner. We can combine it with a """ + L("real-estate-property-manager", "property maintenance visit") + """.</p>
<p>For the broader picture on repairs versus replacement, start at the """ + L("hot-water", "hot water systems page") + """. If your unit is leaking rather than misbehaving, use the """ + H("urgent hot water repairs page") + """ has the steps for cutting power and water first. Company details are on """ + M("moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Tempering valves and thermostatic mixing valves</h2>
<p>People use the two names interchangeably, but they are different devices. A tempering valve is the standard fitting on a domestic hot water outlet and holds the supply at a safe bathroom temperature within a modest tolerance. A thermostatic mixing valve reacts faster and holds a tighter temperature, which is why aged care, child care, hospitals and some disability modifications require one, along with scheduled testing. If a bathroom modification or a care plan calls for a thermostatic mixing valve rather than a tempering valve, we fit and commission it to that requirement and record the test results.</p>
"""),
    faqs=[
        ("Can I adjust the tempering valve myself?",
         "<p>The adjustment is capped and sealed for a reason: set too high it allows scalding water into the bathroom. In Queensland the work sits with a licensed plumber, who sets it with a thermometer and records the result.</p>"),
        ("Does a continuous flow gas unit need a tempering valve?",
         "<p>Many continuous flow units control outlet temperature electronically and can be set to a safe bathroom temperature, but the installation still has to meet the standard. We check the model and the layout and advise accordingly.</p>"),
        ("Why is my kitchen tap hotter than my shower?",
         "<p>The kitchen supply usually branches off before the tempering valve, so it arrives untempered. The bathroom supply is tempered. That difference is by design, not a fault.</p>"),
    ],
    related=[
        ("hot-water", "Hot water systems"),
        ("water-compliancy", "Water compliance for rentals"),
        ("real-estate-property-manager", "Property manager plumbing"),
        ("hot-water-gold-coast", "Hot water Gold Coast"),
        ("hot-water-springwood", "Hot water Springwood"),
    ],
)
