#import "@preview/polylux:0.3.1": *
#import themes.clean: *
// #import emoji: clapperboard

#set page(paper: "presentation-16-9", fill: lime.lighten(90%))
#set text(size: 20pt, font: "Inria Sans")

// #show: simple-theme.with(
//   footer: [Simple slides],
// )
#show link: underline
#show link: set text(blue)
#show: clean-theme.with(
    footer: [Andreas Kröpelin, July 2023],
    short-title: [Polylux demo],
    // logo: image("../assets/logo.png"),
)
// #enable-handout-mode(true)

#title-slide(
    title: [Numerical Methods for Ordinary Differential Equations],
    subtitle: "with JAX (Python programming language)",
    authors: "Ugrd. Carlos Aznarán",
    date: "December 2023",
)
// https://cu-numpde.github.io/fall22/
#new-section-slide("Introduction")

// #title-slide[
//   #v(2em)

//   #footnote[National University of Engineering] #h(1em)

//   https://t.me/s/advection_diffusion

//   https://www.youtube.com/@Advection-Diffusion_Equation

//   #emoji.face

//   Last modification: #datetime.today().display()
// ]

#slide[
  == First slide

  #lorem(20)
]

#focus-slide[
  _Focus!_

  This is very important.
]

// #centered-slide[
//   = Let's start a new section!
// ]

#slide[
  == Dynamic slide
  Did you know that...

  #pause
  ...you can see the current section at the top of the slide?

  $ lim 1/x = oo $

  I got an ice cream for \$1.50! \u{1f600}
]

// #polylux-slide[
//   == Outline

//     // Textbook: https://textbooks.open.tudelft.nl/textbooks/catalog/book/57

//     // - The links showed will be there in the Telegram Channel (open access).
//     // - The recorded will there in YouTube.

//     \

//   #line-by-line(mode: "transparent")[
//     - Introduction to Numerical Mathematics
//     - Floating point numbers
//     - Interpolation
//     - Numerical differenciation
//     - Nonlinear equations
//     - Numerical integration
//     - Numerical time integration of initial-value problems
//     - Finite-difference method for boundary-value problems
//     - The instationary heat equation
//   ]
// ]

// #polylux-slide[
//   == This slide changes!

//   You can always see this. #pause
//   // Make use of features like #uncover, #only, and others to create dynamic content
//   #uncover(2)[But this appears later!]
// ]