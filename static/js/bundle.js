(()=>{
    "use strict";
    var i = {
        138: (i,t,s)=>{
            class h {
                constructor(i={}) {
                    this.isRain = i.isRain || !1,
                    this.el = null,
                    this.dir = i.dir || "r",
                    this.width = 0,
                    this.maxWidth = i.maxWidth || 80,
                    this.minWidth = i.minWidth || 2,
                    this.opacity = 0,
                    this.x = 0,
                    this.y = 0,
                    this.z = 0,
                    this.sx = 0,
                    this.isSwing = !1,
                    this.stepSx = .02,
                    this.swingRadian = 1,
                    this.swingStep = .01,
                    this.sy = 0,
                    this.maxSpeed = i.maxSpeed || 4,
                    this.minSpeed = i.minSpeed || 1,
                    this.quickMaxSpeed = i.quickMaxSpeed || 10,
                    this.quickMinSpeed = i.quickMinSpeed || 8,
                    this.quickWidth = i.quickWidth || 80,
                    this.quickOpacity = i.quickOpacity || .2,
                    this.windowWidth = window.innerWidth,
                    this.windowHeight = window.innerHeight,
                    this.init()
                }
                init(i) {
                    let t = Math.random() > .8;
                    this.isSwing = Math.random() > .8,
                    this.width = t ? this.quickWidth : Math.floor(Math.random() * this.maxWidth + this.minWidth),
                    this.opacity = t ? this.quickOpacity : Math.random(),
                    this.x = Math.floor(Math.random() * (this.windowWidth - this.width)),
                    this.y = Math.floor(Math.random() * (this.windowHeight - this.width)),
                    i && Math.random() > .8 ? this.x = -this.width : i && (this.y = -this.width),
                    this.sy = t ? Math.random() * this.quickMaxSpeed + this.quickMinSpeed : Math.random() * this.maxSpeed + this.minSpeed,
                    this.sx = "r" === this.dir ? this.sy : -this.sy,
                    this.z = t ? 300 * Math.random() + 200 : 0,
                    this.swingStep = .01 * Math.random(),
                    this.swingRadian = Math.random() * (1.1 - .9) + .9
                }
                setStyle() {
                    this.el.style.cssText = `\n            position: fixed;\n            left: 0;\n            top: 0;\n            display: block;\n            width: ${this.isRain ? 1 : this.width}px;\n            height: ${this.width}px;\n            opacity: ${this.opacity};\n            background-image: radial-gradient(#fff 0%, rgba(255, 255, 255, 0) 60%);\n            border-radius: 50%;\n            z-index: 9999999999999;\n            pointer-events: none;\n            transform: translate(${this.x}px, ${this.y}px) ${this.getRotate(this.sy, this.sx)};\n        `
                }
                render() {
                    this.el = document.createElement("div"),
                    this.setStyle(),
                    document.body.appendChild(this.el)
                }
                move() {
                    this.isSwing ? ((this.swingRadian > 1.1 || this.swingRadian < .9) && (this.swingStep = -this.swingStep),
                    this.swingRadian += this.swingStep,
                    this.isRain ? this.x += this.sx : this.x += this.sx * Math.sin(this.swingRadian * Math.PI),
                    this.y -= this.sy * Math.cos(this.swingRadian * Math.PI)) : (this.x += this.sx,
                    this.y += this.sy),
                    (this.x < -this.width || this.x > this.windowWidth || this.y > this.windowHeight) && (this.init(!0),
                    this.setStyle()),
                    this.el.style.transform = `translate3d(${this.x}px, ${this.y}px, ${this.z}px) ${this.getRotate(this.sy, this.sx)}`
                }
                getRotate(i, t) {
                    return this.isRain ? `rotate(${0 === t ? 0 : 90 + Math.atan(i / t) * (180 / Math.PI)}deg)` : ""
                }
            }
            class n {
                constructor(i={}) {
                    this.num = i.num || 100,
                    this.opt = i,
                    this.snowList = [],
                    this.createSnows(),
                    this.moveSnow()
                }
                createSnows() {
                    this.snowList = [];
                    for (let i = 0; i < this.num; i++) {
                        let i = new h(this.opt);
                        i.render(),
                        this.snowList.push(i)
                    }
                }
                moveSnow() {
                    window.requestAnimationFrame((()=>{
                        this.snowList.forEach((i=>{
                            i.move()
                        }
                        )),
                        this.moveSnow()
                    }
                    ))
                }
            }
            new n({
                isRain: !0,
                num: 300,
                maxSpeed: 15
            }),
            new n({
                isRain: !1,
                num: 150
            })
        }
    }
      , t = {};
    function s(h) {
        if (t[h])
            return t[h].exports;
        var n = t[h] = {
            exports: {}
        };
        return i[h](n, n.exports, s),
        n.exports
    }
    s.d = (i,t)=>{
        for (var h in t)
            s.o(t, h) && !s.o(i, h) && Object.defineProperty(i, h, {
                enumerable: !0,
                get: t[h]
            })
    }
    ,
    s.o = (i,t)=>Object.prototype.hasOwnProperty.call(i, t),
    s(138)
}
)();