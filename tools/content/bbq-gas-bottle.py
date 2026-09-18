from _common import *

page = dict(
    slug="bbq-gas-bottle", kind="service", crumb="BBQ gas",
    title="BBQ Gas Bayonet & Bottle Connections | Moyle Plumbing",
    description='BBQ gas connections on the northern Gold Coast: bayonet points, LPG bottle installs and safety checks by licensed gasfitters. Call (07) 3807 7327.',
    h1="BBQ gas connections and bottle installations",
    eyebrow="Outdoor gas",
    intro="<p>BBQ gas connections done properly mean no more swapping bottles at the servo and no more wondering whether that hiss is normal. Moyle Plumbing &amp; Gasfitting's licensed gasfitters install bayonet points, connect barbecues and outdoor kitchens to natural gas or LPG, and set up bottle installations across the northern Gold Coast and Logan.</p>",
    breadcrumb=[("all-services-available", "Services"), ("gas-fitting", "Gas fitting")],
    service=dict(name="BBQ gas connections", area="Gold Coast"),
    body=sec("""
<h2>Options for outdoor gas</h2>
<div class="two-col">
<div>
<h3>Homes with natural gas</h3>
<p>We run a line from the existing installation to a bayonet point on the patio or outdoor kitchen. The barbecue connects with a hose and bayonet plug, and disconnects in a second when you want to move it. The appliance must be a natural gas model or converted by the manufacturer's kit.</p>
</div>
<div>
<h3>Homes on LPG</h3>
<p>Either a bayonet run from the home's cylinders, or a dedicated 9 kg bottle at the barbecue with a proper regulator and hose. For outdoor kitchens with several burners, a larger exchange cylinder installation at the side of the house with a fixed line is safer and cheaper to run.</p>
</div>
</div>
""") + soft("""
<h2>What a licensed connection includes</h2>
<ul class="checks">
<li>Pipe sized for the appliance, with an isolation valve you can reach.</li>
<li>A bayonet point mounted where the hose will not cross a walkway or lie against hot surfaces.</li>
<li>The correct regulator for the gas type and appliance pressure.</li>
<li>A leak test of the new line and every joint, then a burner test on the appliance.</li>
<li>Compliance documentation for the gas work.</li>
</ul>
<p>Fixed gas installations are licensed work in Queensland. That includes running a line to a bayonet. Screwing a regulator onto a swap-and-go bottle for a portable barbecue is the only part a homeowner should be doing.</p>
""") + sec("""
<h2>Bottle safety at home</h2>
<ul>
<li>Cylinders stay upright, outdoors, on a firm base, away from drains and ignition sources.</li>
<li>Check the hose for cracks each season and replace it if in doubt.</li>
<li>Test connections with soapy water after every bottle change: bubbles mean a leak.</li>
<li>Never use a cylinder past its stamped test date; exchange programs handle retesting for you.</li>
<li>If you smell gas at the barbecue, close the cylinder valve first, then step away.</li>
</ul>
""" + callout("<p>A gas smell inside the house is treated differently: shut it at the meter or cylinder, air the place out, leave the switches alone, step outside and ring us. The " + H("gas emergency steps") + " has the full sequence.</p>", warn=True) + """
<p>Outdoor kitchens often need a hot water point and a sink drain as well as gas, which is everyday work for a plumber and gasfitter in one. Larger LPG installations for cooking and hot water sit under """ + L("gas-fitting", "gas fitting") + """, and gas hot water options are on the """ + L("hot-water", "hot water page") + """. Cafes with outdoor cooking come under """ + L("commercial-plumbing", "commercial plumbing") + """. We do this work in """ + L("plumber-pimpama", "Pimpama") + """, """ + L("plumber-ormeau", "Ormeau") + """, Coomera and Helensvale; the business behind it is """ + M("our Yatala gasfitters' main site") + """.</p>
""") + sec("""
<h2>Outdoor kitchens: the whole package</h2>
<p>An outdoor kitchen usually needs more than a gas point. There is a sink with hot and cold water, a drain that has to reach the sewer or a gully, sometimes a dishwasher or bar fridge with an ice maker, and a fire pit or heater on a second bayonet. Getting the pipes in before the slab is poured or the cabinetry is fixed saves cutting later, so we like to see the plan early. On the gas side, several burners plus a wok and a pizza oven can add up to a load that a standard 9 kg bottle cannot supply for long, which is when a fixed twin-cylinder installation earns its keep.</p>
"""),
    faqs=[
        ("Can I connect my LPG barbecue to natural gas?",
         "<p>Only if the manufacturer offers a conversion kit for that model, fitted and tested by a licensed gasfitter. The burners and injectors differ between gas types, and running the wrong gas is dangerous.</p>"),
        ("How far can the bayonet be from the gas meter?",
         "<p>Distance is not the limit; pipe sizing is. A longer run needs a larger pipe to deliver the pressure the appliance needs. We size it during the site visit.</p>"),
        ("Is a bayonet safe if the barbecue is unplugged?",
         "<p>Yes. The bayonet socket seals when the plug is removed. Turn off the isolation valve as well when the barbecue is put away for a long period.</p>"),
    ],
    related=[
        ("gas-fitting", "Gas fitting"),
        ("hot-water", "Hot water systems"),
        ("commercial-plumbing", "Commercial plumbing"),
        ("plumber-pimpama", "Plumber Pimpama"),
        ("plumber-ormeau", "Plumber Ormeau"),
    ],
)
