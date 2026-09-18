from _common import *

page = dict(
    slug="leak-repairs", kind="service", crumb="Leak repairs",
    title="Water Leak Detection & Repair Gold Coast | Moyle Plumbing",
    description='Water leak detection and repair for the northern Gold Coast and Logan. Concealed leaks under slabs and in walls found first. Call (07) 3807 7327.',
    h1="Water leak detection and repair",
    eyebrow="Concealed leaks",
    intro="<p>Water leak detection and repair is about finding the leak before you start digging or cutting. A concealed leak can run for months, quietly adding to the water bill and soaking a slab or wall frame. Moyle Plumbing &amp; Gasfitting locates concealed leaks across the northern Gold Coast using test equipment rather than trial and error, then repairs them with the price agreed first.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Water leak detection and repair", area="Gold Coast"),
    body=sec("""
<h2>Signs you have a hidden leak</h2>
<ul class="checks">
<li>The water meter dial keeps creeping with every tap and appliance off.</li>
<li>A water bill that has climbed with no change in how the household uses water.</li>
<li>A patch of floor that is warm underfoot, which usually means the hot water line under the slab.</li>
<li>Paint bubbling, skirting swelling or a musty smell in one room.</li>
<li>A wet spot in the lawn that never dries out, or grass that grows greener along one line.</li>
<li>The hot water system running more than it used to, or the pump on a tank supply cycling on and off overnight.</li>
</ul>
<h2>The ten-minute meter test</h2>
<p>Turn off every tap, the washing machine, dishwasher, irrigation and the toilet cisterns' isolation valves. Write down the meter reading, small dial included. Wait ten minutes with everything still off, then read it again. Movement means water is escaping somewhere past the meter. Then turn the hot water unit's isolation tap off and repeat: if the movement stops, the leak is on the hot side.</p>
""") + soft("""
<h2>How we find it</h2>
<ol class="steps">
<li><strong>Pressure test</strong> hot and cold separately to establish which side is losing water and roughly how fast.</li>
<li><strong>Acoustic listening</strong> along the pipe route to hear the leak through the slab or wall.</li>
<li><strong>Thermal imaging</strong> to see warm water spreading under a floor or through a wall cavity, which is quick and decisive on hot lines.</li>
<li><strong>Tracer gas</strong> for stubborn cases, where a safe gas mix is pushed through the line and detected where it escapes.</li>
<li><strong>Camera inspection</strong> where the leak is on a drain rather than a pressure pipe.</li>
</ol>
<p>The result is a marked spot, not a guess, so the repair opening is as small as possible. On some jobs the sensible fix is to abandon the leaking section under the slab and reroute the pipe through the wall or ceiling, and we will tell you when that is the cheaper option.</p>
""") + sec("""
<h2>Leaks by location</h2>
<table>
<thead><tr><th>Where</th><th>Likely cause</th><th>Typical fix</th></tr></thead>
<tbody>
<tr><td>Under a slab</td><td>Corroded or damaged copper</td><td>Locate and repair, or reroute</td></tr>
<tr><td>Inside a wall</td><td>Failed joint, nail through pipe, mixer tap body</td><td>Open, replace section, close</td></tr>
<tr><td>Ceiling</td><td>Upstairs bathroom waste, shower tray, roof plumbing</td><td>Trace and reseal or replace</td></tr>
<tr><td>Yard</td><td>Poly main, irrigation, garden tap</td><td>Excavate small area and repair</td></tr>
<tr><td>Shower recess</td><td>Failed waterproofing or grout, not the pipe</td><td>See """ + L("leaking-shower-repairs", "leaking shower repairs") + """</td></tr>
</tbody>
</table>
<p>If the leak has just become a running burst, turn off the meter and go to the """ + L("burst-pipe", "burst pipe page") + """. Water coming through a light fitting or onto a switchboard is urgent: the """ + H("urgent leak repair page") + """ home page covers what to shut off. Leaking toilets are covered under """ + L("toilets", "toilet repairs") + """, and leak and fixture checks form part of our """ + L("water-compliancy", "water compliance checks") + """ for rentals.</p>
<p>Moyle Plumbing, a family business since 1983 working out of Yatala throughout, is described on the """ + M("Moyle Plumbing") + """ site.</p>
"""),
    faqs=[
        ("Will you have to dig up the slab?",
         "<p>Not always. Once the leak is located we weigh up a small opening at the exact spot against rerouting the pipe above the slab. Rerouting often wins on cost and disruption, especially on hot water lines.</p>"),
        ("Can a leak be on the council side?",
         "<p>Yes. Anything before the meter belongs to the water utility. If the meter is not moving but the footpath or verge is wet, report it to your water provider. Anything after the meter is the property owner's.</p>"),
        ("How accurate is leak detection?",
         "<p>On most jobs the location is marked within a small area, close enough to open a single tile or a short section of wall. The accuracy depends on pipe depth, material and background noise, and we tell you how confident we are before cutting.</p>"),
        ("Do you repair the wall or floor afterwards?",
         "<p>We make good the plumbing and leave the area clean. Tiling, plastering and painting are separate trades, and we can advise what will be needed so you can arrange it.</p>"),
    ],
    related=[
        ("burst-pipe", "Burst pipe repair"),
        ("leaking-shower-repairs", "Leaking shower repairs"),
        ("toilets", "Toilet repairs"),
        ("water-compliancy", "Water compliance"),
        ("plumber-hope-island", "Plumber Hope Island"),
        ("plumber-shailer-park", "Plumber Shailer Park"),
        ("plumber-rochedale-south", "Plumber Rochedale South"),
    ],
)
