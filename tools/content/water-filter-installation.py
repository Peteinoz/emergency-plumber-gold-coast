from _common import *

page = dict(
    slug="water-filter-installation", kind="service", crumb="Water filters",
    title="Water Filter Installation Gold Coast | Moyle Plumbing",
    description='Water filter installation by licensed plumbers on the northern Gold Coast and Logan. Under-sink, whole-house and tank filters. Call (07) 3807 7327.',
    h1="Water filter installation",
    eyebrow="Filtration",
    intro="<p>Water filter installation done by a licensed plumber means a system that is connected correctly, does not leak under the bench and can be serviced without a fight. Moyle Plumbing &amp; Gasfitting installs under-sink, benchtop-connected, whole-house and rainwater tank filters across the northern Gold Coast and Logan.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Water filter installation", area="Gold Coast"),
    body=sec("""
<h2>Which filter for which problem</h2>
<table>
<thead><tr><th>You want to</th><th>Usual system</th></tr></thead>
<tbody>
<tr><td>Improve taste and remove chlorine from town water at the kitchen tap</td><td>Under-sink carbon filter with a separate drinking tap or a three-way mixer</td></tr>
<tr><td>Remove sediment and protect appliances across the whole house</td><td>Whole-house sediment and carbon cartridge housing at the meter or main entry</td></tr>
<tr><td>Make rainwater tank water safe for drinking</td><td>Sediment plus fine filtration and UV disinfection on the house supply</td></tr>
<tr><td>Deal with hard water scale on hot water systems and taps</td><td>Scale inhibitor or water conditioner on the incoming main</td></tr>
<tr><td>Instant filtered boiling and chilled water</td><td>Dedicated boiling and chilled unit with its own filter and drain</td></tr>
</tbody>
</table>
<p>Mains water across the Gold Coast is treated and safe, so most household filters are about taste, chlorine and sediment rather than safety. Tank water is a different matter and needs proper treatment before anyone drinks it.</p>
""") + soft("""
<h2>What the installation includes</h2>
<ul class="checks">
<li>A dedicated isolation valve so the filter can be changed without shutting the kitchen down.</li>
<li>A pressure check, with a limiting valve fitted if mains pressure exceeds what the filter housing is rated for.</li>
<li>A drinking tap drilled and fitted into the sink or benchtop where required, sealed properly.</li>
<li>Housings mounted so cartridges can be swapped by hand, not wedged behind the bin.</li>
<li>Flushing and testing under pressure before we leave, with the change-out date written on the housing.</li>
</ul>
""") + sec("""
<h2>Filters on rainwater tanks</h2>
<p>Acreage homes around Alberton, Mount Cotton and Ormeau Hills often live entirely on tank water. A first-flush diverter and tank screen keep the worst out, but the house supply still benefits from a sediment stage, a finer filter and, if the water is for drinking, UV treatment. We fit filtration on the pressure side of the pump with bypass valves, so a blocked cartridge never leaves the house without water. Pump sizing and filtration go together: see """ + L("pumps", "pump repairs and installation") + """.</p>
<h2>Servicing</h2>
<p>Cartridges have a working life measured in months, and UV lamps in about a year. A filter that has not been changed is worse than no filter. We can replace cartridges on a schedule for households and rentals, or show you how to do it yourself.</p>
<p>The same kitchen visit can include a """ + L("dishwasher-installations", "dishwasher") + """ or an """ + L("insinkerator", "InSinkErator") + """ hook-up, or any of the small jobs under """ + L("general-plumbing-maintenance", "plumbing maintenance") + """. Filters are not urgent work, but a housing that has cracked and is spraying under the bench is; the """ + H("burst fitting emergency page") + """ page shows what to shut. We fit filters across """ + L("plumber-hope-island", "Hope Island") + """, """ + L("plumber-helensvale", "Helensvale") + """, Coomera and Pimpama. Business details at """ + M("moyleplumbing.com.au") + """.</p>
""") + sec("""
<h2>Boiling and chilled water units</h2>
<p>Under-bench units that deliver instant boiling, chilled and sparkling water are common in renovated kitchens and in offices. They need a cold water point with isolation, a drain connection for the drip tray and the unit's own filter, plus a power point and enough cabinet ventilation for the compressor. We install them with the plumbing in the right cabinet so the unit is serviceable, and we can take over the filter change schedule for offices where nobody remembers whose job it is. If you are planning a kitchen, mention the unit early so the point lands where the manufacturer specifies.</p>
"""),
    faqs=[
        ("Can a filter be added to my existing mixer tap?",
         "<p>Yes, either by replacing the mixer with a three-way model that has a separate filtered outlet, or by adding a small dedicated filter tap beside it. Both are common and the choice comes down to the sink and the look you want.</p>"),
        ("Do I need a filter on Gold Coast town water?",
         "<p>Not for safety. Many people fit one for taste and to remove chlorine, and a whole-house sediment filter can extend the life of appliances. It is a preference rather than a requirement.</p>"),
        ("Will a whole-house filter reduce my water pressure?",
         "<p>A correctly sized housing has very little effect. Undersized housings and cartridges left in too long are what cause pressure loss, and both are avoidable.</p>"),
        ("How often do cartridges need changing?",
         "<p>It depends on the cartridge and the water. Follow the manufacturer's interval, usually somewhere between six and twelve months, and sooner on tank water with a lot of sediment.</p>"),
    ],
    related=[
        ("dishwasher-installations", "Dishwasher installation"),
        ("insinkerator", "InSinkErator installation"),
        ("general-plumbing-maintenance", "Plumbing maintenance"),
        ("pumps", "Pumps"),
        ("plumber-hope-island", "Plumber Hope Island"),
        ("plumber-helensvale", "Plumber Helensvale"),
    ],
)
