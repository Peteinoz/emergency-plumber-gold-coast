from _common import *

page = dict(
    slug="plumber-mount-cotton", kind="suburb", crumb="Plumber Mount Cotton",
    title="Plumber Mount Cotton | Acreage, Tanks & Pumps | Moyle",
    description="Plumber for Mount Cotton acreage: rainwater tanks, pressure pumps, filtration, septic and treatment plant plumbing, hot water and gas. Call (07) 3807 7327.",
    h1="Plumber Mount Cotton: acreage plumbing done properly",
    eyebrow="Mount Cotton QLD 4165",
    intro="<p>A plumber in Mount Cotton has to understand a household that makes its own water and treats its own waste. Most of the suburb is acreage on rainwater tanks with pressure pumps, and on septic tanks or home treatment plants. Moyle Plumbing &amp; Gasfitting comes across from Yatala for that work and for the ordinary indoor plumbing, with the price set before we start.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Plumbing services in Mount Cotton", area="Mount Cotton"),
    body=sec("""
<h2>The tank water household, part by part</h2>
<ol class="steps">
<li><strong>Roof and gutters.</strong> Everything starts here. First-flush diverters and leaf screens keep the worst out of the tank; blocked ones send dirty water in.</li>
<li><strong>The tank.</strong> Inlet strainers, overflow screens and the outlet position all affect water quality. A tank that has never been cleaned has a layer of sludge that a low outlet will pull into the house.</li>
<li><strong>The pump.</strong> A pressure pump with a controller gives the house its pressure. Dry-run protection stops it burning out when the tank empties. Sizing matters: too small and the second shower starves, too big and it short-cycles.</li>
<li><strong>Filtration.</strong> A sediment filter at minimum, finer filtration and UV where the water is for drinking. Cartridges must be changed on schedule.</li>
<li><strong>Mains changeover.</strong> Where town water is available, an automatic changeover keeps the house supplied when the tank runs low.</li>
<li><strong>Hot water.</strong> Tank water and pump pressure affect which hot water units work well; some continuous flow units need a minimum flow the pump must deliver.</li>
</ol>
<p>Pump faults and replacement are on the """ + L("pumps", "pumps page") + """; filtration on the """ + L("water-filter-installation", "water filters page") + """.</p>
""") + soft("""
<h2>Septic tanks and treatment plants</h2>
<p>Household drainage runs to a septic tank with absorption trenches, or to an aerated treatment plant with irrigation. Both need the plumbing to them kept clear and the pump-outs done. Slow drains throughout the house, wet ground over the trenches or an alarm on the plant are the warning signs. We handle the house drains, effluent pumps, plant plumbing and the arrangements for pump-out; see """ + L("blocked-drains", "blocked drains") + """ for how a blockage is diagnosed on an on-site system.</p>
<h2>Bush blocks and bushfire season</h2>
<p>Mount Cotton's blocks back onto bushland. Homeowners often ask us about dedicated fire-fighting outlets on tanks, bushfire pumps and the fittings the rural fire brigade can connect to. We can plumb tank outlets and standpipes for that purpose as part of a tank setup.</p>
""") + sec("""
<h2>Everything else</h2>
<p>Indoors it is the usual work: hot water, taps, toilets, gas cooktops on LPG, renovations and leaks. The difference is that a leak on a tank property is not just a bill, it is water you cannot get back, so the pump cycling at night is worth chasing early. See """ + L("leak-repairs", "leak detection") + """. A tank property with no water is urgent; the """ + H("Mount Cotton emergency plumber page") + """ page covers what to check first. We also work in """ + L("plumber-redland-bay", "Redland Bay") + """ and across the Redlands, and in """ + L("plumbing-services-alberton", "Alberton") + """ on the other side of the highway. More on the business is at """ + M("www.moyleplumbing.com.au") + """.</p>
"""),
    faqs=[
        ("My pump runs but the pressure is poor. What is wrong?",
         "<p>Check the tank level and the filter cartridges first. A blocked filter or a nearly empty tank are the usual causes. If both are fine, the pump may have lost prime, the foot valve may be blocked or the impeller worn.</p>"),
        ("How often should tank filters be changed?",
         "<p>Follow the cartridge maker's interval and change sooner if pressure drops. Tank water carries more sediment than town water, so intervals are often shorter than the packet suggests.</p>"),
        ("Can you connect town water as a backup to my tank?",
         "<p>Where a mains connection exists, yes. An automatic changeover valve switches the house to mains when the tank is low and back when it refills, with backflow protection to keep tank water out of the mains.</p>"),
        ("Do you service aerated treatment plants?",
         "<p>We handle the plumbing, pumps and drainage connected to the plant. The plant's own periodic service is usually done by the manufacturer's agent, and we can tell you if something we see needs their attention.</p>"),
    ],
    related=[
        ("pumps", "Pumps"),
        ("water-filter-installation", "Water filters"),
        ("blocked-drains", "Blocked drains"),
        ("leak-repairs", "Leak detection"),
        ("hot-water", "Hot water"),
        ("plumber-redland-bay", "Plumber Redland Bay"),
        ("plumbing-services-alberton", "Plumbing Alberton"),
    ],
)
