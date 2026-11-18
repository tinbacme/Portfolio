// ATS-friendly resume (Word). Rules followed, from ATS formatting research:
// one column; no tables, text boxes, images, headers or footers; contact info in the body with text labels and visible URLs;
// standard headings (Summary, Experience, Education, Skills); one role per entry with title, company and dates together;
// one date format (YYYY – YYYY / Present) set with a right tab stop; real Word bullets; one standard font (Calibri).
// usage: node make-docx.js  -> Tin-Le-Resume.docx
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, TabStopType, BorderStyle, ExternalHyperlink, LevelFormat, HeadingLevel, AlignmentType } = require('docx');
const FONT = 'Calibri', INK = '000000', MUT = '444444';
const W = 12240, M = 1080, RIGHT = W - 2 * M;
const run = (text, o = {}) => new TextRun({ text, font: FONT, size: o.size || 21, bold: !!o.bold, italics: !!o.i, color: o.color || INK });
const heading = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [run(t.toUpperCase(), { size: 22, bold: true })] });
const role = (title, company, dates) => new Paragraph({ spacing: { before: 110, after: 20 }, keepNext: true, tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
  children: [run(title, { bold: true }), run(', ' + company), run('\t' + dates)] });
const bullet = (t) => new Paragraph({ numbering: { reference: 'dots', level: 0 }, spacing: { after: 30 }, children: [run(t, { color: MUT })] });
const link = (url, label) => new ExternalHyperlink({ link: url, children: [new TextRun({ text: label, font: FONT, size: 20, color: '1155CC', underline: {} })] });
const skill = (k, v) => new Paragraph({ spacing: { after: 30 }, children: [run(k + ': ', { bold: true }), run(v, { color: MUT })] });

const doc = new Document({
  creator: 'Tin Le', title: 'Tin Le Resume',
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [{ id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
      run: { font: FONT, size: 22, bold: true, color: INK },
      paragraph: { spacing: { before: 220, after: 70 }, keepNext: true, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '999999', space: 2 } } } }],
  },
  numbering: { config: [{ reference: 'dots', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] }] },
  sections: [{ properties: { page: { size: { width: W, height: 15840 }, margin: { top: 760, bottom: 720, left: M, right: M } } }, children: [
    new Paragraph({ spacing: { after: 40 }, children: [run('Tin Le', { size: 40, bold: true })] }),
    new Paragraph({ spacing: { after: 40 }, children: [run('Senior Product Designer', { size: 23, color: MUT })] }),
    new Paragraph({ spacing: { after: 0 }, children: [run('Email: ', { size: 20, color: MUT }), link('mailto:tinbacme@gmail.com', 'tinbacme@gmail.com'),
      run('  |  LinkedIn: ', { size: 20, color: MUT }), link('https://www.linkedin.com/in/letin08/', 'linkedin.com/in/letin08')] }),

    heading('Summary'),
    new Paragraph({ spacing: { after: 40 }, children: [run('Senior Product Designer at Microsoft AI who also teaches product design at the University of Oregon. Trained in industrial design, so building and prototyping is how I work every day, from search experiences and design systems to physical products.', { color: MUT })] }),

    heading('Experience'),
    role('Senior Product Designer', 'Microsoft AI', '2022 – Present'),
    bullet('Design search across Bing, Edge and Windows: helping people find what they need, growing Bing, and exploring what AI agents could do in search.'),
    bullet('Work is under NDA; happy to walk through it in an interview.'),

    role('Product Design Instructor', 'University of Oregon', '2023 – Present'),
    bullet('Teach a 12-week course in UX research, UX/UI design and prototyping, at the school where I studied industrial design.'),

    role('UX/UI Bootcamp Instructor', '2U', '2021 – Present'),
    bullet('Lead cohorts through a 24-week bootcamp in UX research, UX and UI design and front-end development.'),
    bullet('Taught with the University of Oregon, UC Berkeley, Michigan, Minnesota, Utah and Arizona.'),

    role('Designer', 'Salesforce', '2020 – 2022'),
    bullet('Redesigned search and content for Salesforce Help, cutting support cases by 60% per month.'),
    bullet('Built a back-to-work app used by 75K employees.'),
    bullet('Shipped 8+ Partner Community features.'),
    bullet('Added components to the C360 design system used across 12 product teams.'),

    role('Associate Designer', 'Salesforce', '2018 – 2020'),
    bullet('Worked with stakeholders to map customer experiences, find pain points and spot opportunities.'),
    bullet('Designed wireframe concepts with the Salesforce Lightning Design System.'),

    role('Product Design Intern', 'Salesforce', '2017'),
    bullet('Redesigned onboarding for new employees with a portal to access information, search for benefits and manage their profiles.'),
    bullet('Designed the branding for a Salesforce hackathon.'),

    role('Product Designer', 'Luxium Lighting', '2017'),
    bullet('Took an LED light from concept to working prototype.'),

    heading('Education'),
    role('BS Industrial Design, Business Minor', 'University of Oregon', '2014 – 2018'),
    bullet('Sketching, CAD, rendering and building prototypes by hand.'),
    bullet('1st place overall, Quackhatch @UO 2018.'),

    heading('Skills'),
    skill('Design', 'Product design, UX/UI design, interaction design, search experiences, design systems (C360, Salesforce Lightning Design System), wireframing, prototyping'),
    skill('Research', 'UX research, customer journey mapping, stakeholder collaboration'),
    skill('Industrial design', 'Sketching, CAD, rendering, physical prototyping'),
    skill('Teaching', 'Course design and instruction in UX research, UX/UI design, prototyping and front-end development'),
  ] }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(__dirname + '/Tin-Le-Resume.docx', b); console.log('ok', b.length); });
