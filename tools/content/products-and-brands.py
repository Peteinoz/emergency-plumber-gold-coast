from _common import *

page = dict(
    slug="products-and-brands", kind="core", crumb="Products and brands",
    title="Plumbing & Hot Water Brands We Service | Moyle Plumbing",
    description='Hot water, tapware, toilet and appliance brands found in Gold Coast homes, serviced and supplied by Moyle Plumbing. Call (07) 3807 7327.',
    h1="Plumbing and hot water brands we supply and service",
    eyebrow="Products and brands",
    intro="<p>The plumbing and hot water brands in a typical Gold Coast house are a mix of what the builder fitted, what the last owner chose and what was on special at the time. Moyle Plumbing &amp; Gasfitting works on all of the major brands sold in Australia, carries common parts for them, and supplies new products from manufacturers whose parts and support we can rely on.</p>",
    breadcrumb=[],
    body=sec("""
<h2>Hot water systems</h2>
<p>Storage, continuous flow, heat pump and solar units from the major Australian and imported makers. On a repair we identify the model from its plate, carry elements, thermostats and valves that fit most units, and order model-specific parts where needed. On a replacement we recommend on capacity, warranty, parts availability and the fit for your home, and explain why. Choices are listed on the """ + L("hot-water", "hot water page") + """.</p>
<h2>Tapware and mixers</h2>
<p>Ceramic cartridges, spindles and seals differ by brand and even by model year. We identify what you have before opening the wall, so premium and imported mixers common in """ + L("plumber-hope-island", "Hope Island") + """ and renovated homes are repaired with the right part rather than a substitute that fails early.</p>
<h2>Toilet suites</h2>
<p>Inlet valves, outlet washers, buttons and seals for the common suites are carried on the van. When a suite is replaced we match the outlet position and choose a dual-flush model with a good water rating; see """ + L("toilets", "toilets") + """.</p>
""") + soft("""
<h2>Kitchen appliances and filtration</h2>
<ul class="checks">
<li>""" + L("insinkerator", "InSinkErator food waste disposers") + """, installed and replaced.</li>
<li>""" + L("dishwasher-installations", "Dishwashers") + """ of any brand, connected to water and drainage.</li>
<li>""" + L("water-filter-installation", "Water filters") + """: under-sink, whole-house, boiling and chilled units, and tank water treatment.</li>
</ul>
<h2>Valves, pumps and gas</h2>
<p>Pressure limiting valves, tempering valves, backflow devices, tank pressure pumps, sewage pumps, regulators and bayonet fittings from the established manufacturers, chosen for parts availability and compliance. See """ + L("pumps", "pumps") + """ and """ + L("gas-fitting", "gas fitting") + """.</p>
""") + sec("""
<h2>How we choose what to supply</h2>
<ol class="steps">
<li><strong>Parts must be obtainable.</strong> A product nobody can get parts for in five years is a bad buy however cheap it is.</li>
<li><strong>The warranty must be honoured locally.</strong> We favour brands with service networks in South East Queensland.</li>
<li><strong>It must suit the water and the pressure.</strong> Some products do not cope with the high mains pressure in northern Gold Coast estates without a limiting valve.</li>
<li><strong>It must meet Australian standards.</strong> Plumbing products need WaterMark certification; gas appliances need Australian gas certification. We do not install products without them.</li>
</ol>
<p>If you already have a product in mind, tell us and we will say whether it is a sound choice for your house. Whatever we install carries a firm price before the work starts. When the product that has failed is flooding the laundry, shut things off first using the """ + H("emergency plumbing checklist") + """ steps. Read more about the business on the """ + M("Moyle Plumbing website") + """, or browse the """ + L("all-services-available", "services page") + """.</p>
"""),
    faqs=[
        ("Can I supply my own tapware or hot water unit?",
         "<p>Yes, provided it carries the required Australian certification. We check it suits your pressure and the existing installation before fitting, and tell you if it will not.</p>"),
        ("Do you carry parts for older hot water units?",
         "<p>Elements, thermostats and valves are largely standardised and we carry them. Brand-specific parts for older units are ordered where still made; where they are not, we tell you so before you spend money on a repair.</p>"),
        ("Which brand of hot water system is best?",
         "<p>There is no single answer. The right unit depends on fuel, household size, location and budget. We recommend a specific model for your situation and explain why, rather than pushing one brand.</p>"),
    ],
    related=[
        ("hot-water", "Hot water systems"),
        ("toilets", "Toilets"),
        ("water-filter-installation", "Water filters"),
        ("insinkerator", "InSinkErator"),
        ("pumps", "Pumps"),
        ("about-us", "About us"),
    ],
)
