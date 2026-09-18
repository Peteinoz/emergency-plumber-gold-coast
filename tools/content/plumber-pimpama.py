from _common import *

page = dict(
    slug="plumber-pimpama", kind="suburb", crumb="Plumber Pimpama",
    title="Plumber Pimpama | Moyle Plumbing & Gasfitting, Yatala",
    description="Plumber for Pimpama's new estates, minutes from Yatala. Defects, pressure, hot water, gas and rentals, priced before we start. Call (07) 3807 7327.",
    h1="Plumber Pimpama",
    eyebrow="Pimpama QLD 4209",
    intro="<p>A plumber in Pimpama spends most of the week in houses under ten years old. That is a different job from working on older homes: it is about builder defects, high mains pressure, warranty periods and the first round of replacements. Moyle Plumbing &amp; Gasfitting is at Yatala, one exit up the M1, and knows the estates street by street.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Pimpama", area="Pimpama"),
    body=sec("""
<h2>The first ten years of a new Pimpama home</h2>
<ol class="steps">
<li><strong>Handover to year one.</strong> Defects surface: a floor waste that holds water, a toilet that rocks, a heater plumbed without a tempering valve, a stormwater line full of render. Get them documented while the builder is still liable.</li>
<li><strong>Years two to five.</strong> Mixer cartridges start failing under high pressure. The dishwasher and washing machine hoses need checking. Gas cooktops need their first service.</li>
<li><strong>Years five to ten.</strong> Cheap flexible hoses reach the end of their life. Toilet inlet valves and outlet washers wear. The heater's relief valve begins to dribble.</li>
<li><strong>Year ten onward.</strong> The original hot water unit fails. Owners choose between a like-for-like swap and a heat pump, and the answer depends on the tariff and the roof.</li>
</ol>
<p>A pressure limiting valve fitted early stretches every one of those timelines.</p>
""") + soft("""
<h2>What we are called to in Pimpama</h2>
<ul class="link-grid">
<li>""" + L("hot-water", "Hot water repairs and replacement") + """</li>
<li>""" + L("general-plumbing-maintenance", "Taps, toilets and hoses") + """</li>
<li>""" + L("gas-fitting", "Gas cooktops and continuous flow") + """</li>
<li>""" + L("bbq-gas-bottle", "BBQ bayonet points") + """</li>
<li>""" + L("blocked-drains", "Blocked drains") + """</li>
<li>""" + L("burst-pipe", "Burst flexible hoses") + """</li>
<li>""" + L("dishwasher-installations", "Dishwasher installation") + """</li>
<li>""" + L("real-estate-property-manager", "Rental maintenance") + """</li>
</ul>
<p>Many Pimpama homes are owned by investors and managed by agencies. We work to approval limits, contact tenants directly and report on the cause, which keeps the owner informed without the property manager chasing.</p>
""") + sec("""
<h2>Gas in Pimpama</h2>
<p>Some Pimpama estates were built with reticulated natural gas and others rely on LPG bottles. The appliances, regulators and pipe sizing differ, so mention which one you have when you call. Continuous flow gas hot water is common in the suburb and is a good fit for larger households, provided the gas line was sized for it in the first place; undersized lines are one of the defects we find.</p>
<p>When something has already let go, close the meter or the cylinder valve, then follow the """ + H("Pimpama emergency plumber guidance") + """ from there. Neighbouring """ + L("plumber-ormeau", "Ormeau") + """ and """ + L("plumber-coomera", "Coomera") + """ are covered from the same Yatala base, as is """ + L("plumber-hope-island", "Hope Island") + """ across the highway. Moyle Plumbing has held plumbing and gas licences for decades, and its history is on the """ + M("Moyle Plumbing") + """ site.</p>
""") + sec("""
<h2>Pimpama's drainage after heavy rain</h2>
<p>Parts of Pimpama sit on low, flat land that was farmland not long ago, and it drains slowly. New estates rely on stormwater pits and charged lines to move roof water to the street, and when those are silted from construction the water ends up in the yard or the garage. Sewer lines laid in filled ground can also settle and sag, collecting solids at the low point. If the drains only misbehave after rain, that is the pattern to describe when you ring, because it points us straight to the stormwater and a camera inspection rather than a routine clear.</p>
"""),
    faqs=[
        ("How far is Pimpama from your base?",
         "<p>Pimpama is the next suburb south of Ormeau, which borders Yatala. It is one of the closest areas we serve.</p>"),
        ("Can you document a defect for my builder?",
         "<p>Yes. We look it over, photograph it and describe why it is a defect rather than wear, which is what a builder or the QBCC needs to see.</p>"),
        ("Why do my taps drip so soon after moving in?",
         "<p>High mains pressure combined with basic cartridges. Fitting a pressure limiting valve and better cartridges fixes both the drip and the cause.</p>"),
        ("Do you replace continuous flow gas units?",
         "<p>Yes, and we check the gas line size at the same time, since an undersized line makes a new unit underperform just like the old one.</p>"),
    ],
    related=[
        ("hot-water", "Hot water"),
        ("gas-fitting", "Gas fitting"),
        ("general-plumbing-maintenance", "Plumbing maintenance"),
        ("real-estate-property-manager", "Property managers"),
        ("plumber-ormeau", "Plumber Ormeau"),
        ("plumber-coomera", "Plumber Coomera"),
        ("plumber-hope-island", "Plumber Hope Island"),
    ],
)
