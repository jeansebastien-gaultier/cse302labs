	.text
	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $640, %rsp
	/*   %0 = const 10 [TAC] */
	movq $10, -8(%rbp)
	/*   %1 = const 20 [TAC] */
	movq $20, -16(%rbp)
	/*   %5 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -24(%rbp)
	/*   %6 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -32(%rbp)
	/*   %7 = sub %5, %6 [TAC] */
	movq -24(%rbp), %r11
	subq -32(%rbp), %r11
	movq %r11, -40(%rbp)
	/*   jz %7, %.L2 [TAC] */
	jz .main.L2
	/*   jmp %.L3 [TAC] */
	/* --jmp .main.L3-- */
	/*  %.L3: [TAC] */
.main.L3:
	/*   jmp %.L4 [TAC] */
	jmp .main.L4
	/*  %.L2: [TAC] */
.main.L2:
	/*   %8 = const 0 [TAC] */
	movq $0, -48(%rbp)
	/*   print %8 [TAC] */
	movq -48(%rbp), %rdi
	callq __bx_print_int
	/*  %.L4: [TAC] */
.main.L4:
	/*   %12 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -56(%rbp)
	/*   %13 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -64(%rbp)
	/*   %14 = sub %12, %13 [TAC] */
	movq -56(%rbp), %r11
	subq -64(%rbp), %r11
	movq %r11, -72(%rbp)
	/*   jnz %14, %.L9 [TAC] */
	jnz .main.L9
	/*   jmp %.L10 [TAC] */
	/* --jmp .main.L10-- */
	/*  %.L10: [TAC] */
.main.L10:
	/*   jmp %.L11 [TAC] */
	jmp .main.L11
	/*  %.L9: [TAC] */
.main.L9:
	/*   %15 = const 1 [TAC] */
	movq $1, -80(%rbp)
	/*   print %15 [TAC] */
	movq -80(%rbp), %rdi
	callq __bx_print_int
	/*  %.L11: [TAC] */
.main.L11:
	/*   %20 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -88(%rbp)
	/*   %21 = const 2 [TAC] */
	movq $2, -96(%rbp)
	/*   %19 = mul %20, %21 [TAC] */
	movq -88(%rbp), %rax
	imulq -96(%rbp)
	movq %rax, -104(%rbp)
	/*   %22 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -112(%rbp)
	/*   %23 = sub %19, %22 [TAC] */
	movq -104(%rbp), %r11
	subq -112(%rbp), %r11
	movq %r11, -120(%rbp)
	/*   jz %23, %.L16 [TAC] */
	jz .main.L16
	/*   jmp %.L17 [TAC] */
	/* --jmp .main.L17-- */
	/*  %.L17: [TAC] */
.main.L17:
	/*   jmp %.L18 [TAC] */
	jmp .main.L18
	/*  %.L16: [TAC] */
.main.L16:
	/*   %24 = const 2 [TAC] */
	movq $2, -128(%rbp)
	/*   print %24 [TAC] */
	movq -128(%rbp), %rdi
	callq __bx_print_int
	/*  %.L18: [TAC] */
.main.L18:
	/*   jmp %.L25 [TAC] */
	jmp .main.L25
	/*  %.L28: [TAC] */
.main.L28:
	/*   jmp %.L25 [TAC] */
	jmp .main.L25
	/*  %.L26: [TAC] */
.main.L26:
	/*   jmp %.L27 [TAC] */
	jmp .main.L27
	/*  %.L25: [TAC] */
.main.L25:
	/*   %29 = const 3 [TAC] */
	movq $3, -136(%rbp)
	/*   print %29 [TAC] */
	movq -136(%rbp), %rdi
	callq __bx_print_int
	/*  %.L27: [TAC] */
.main.L27:
	/*   %34 = const 1 [TAC] */
	movq $1, -144(%rbp)
	/*   %35 = const 1 [TAC] */
	movq $1, -152(%rbp)
	/*   %36 = sub %34, %35 [TAC] */
	movq -144(%rbp), %r11
	subq -152(%rbp), %r11
	movq %r11, -160(%rbp)
	/*   jz %36, %.L30 [TAC] */
	jz .main.L30
	/*   jmp %.L33 [TAC] */
	/* --jmp .main.L33-- */
	/*  %.L33: [TAC] */
.main.L33:
	/*   jmp %.L31 [TAC] */
	/* --jmp .main.L31-- */
	/*  %.L31: [TAC] */
.main.L31:
	/*   jmp %.L32 [TAC] */
	jmp .main.L32
	/*  %.L30: [TAC] */
.main.L30:
	/*   %37 = const 4 [TAC] */
	movq $4, -168(%rbp)
	/*   print %37 [TAC] */
	movq -168(%rbp), %rdi
	callq __bx_print_int
	/*  %.L32: [TAC] */
.main.L32:
	/*   %41 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -176(%rbp)
	/*   %42 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -184(%rbp)
	/*   %43 = sub %41, %42 [TAC] */
	movq -176(%rbp), %r11
	subq -184(%rbp), %r11
	movq %r11, -192(%rbp)
	/*   jl %43, %.L38 [TAC] */
	jl .main.L38
	/*   jmp %.L39 [TAC] */
	/* --jmp .main.L39-- */
	/*  %.L39: [TAC] */
.main.L39:
	/*   jmp %.L40 [TAC] */
	jmp .main.L40
	/*  %.L38: [TAC] */
.main.L38:
	/*   %44 = const 5 [TAC] */
	movq $5, -200(%rbp)
	/*   print %44 [TAC] */
	movq -200(%rbp), %rdi
	callq __bx_print_int
	/*  %.L40: [TAC] */
.main.L40:
	/*   %48 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -208(%rbp)
	/*   %49 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -216(%rbp)
	/*   %50 = sub %48, %49 [TAC] */
	movq -208(%rbp), %r11
	subq -216(%rbp), %r11
	movq %r11, -224(%rbp)
	/*   jnle %50, %.L45 [TAC] */
	jnle .main.L45
	/*   jmp %.L46 [TAC] */
	/* --jmp .main.L46-- */
	/*  %.L46: [TAC] */
.main.L46:
	/*   jmp %.L47 [TAC] */
	jmp .main.L47
	/*  %.L45: [TAC] */
.main.L45:
	/*   %51 = const 6 [TAC] */
	movq $6, -232(%rbp)
	/*   print %51 [TAC] */
	movq -232(%rbp), %rdi
	callq __bx_print_int
	/*  %.L47: [TAC] */
.main.L47:
	/*   %55 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -240(%rbp)
	/*   %56 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -248(%rbp)
	/*   %57 = sub %55, %56 [TAC] */
	movq -240(%rbp), %r11
	subq -248(%rbp), %r11
	movq %r11, -256(%rbp)
	/*   jl %57, %.L52 [TAC] */
	jl .main.L52
	/*   jmp %.L53 [TAC] */
	/* --jmp .main.L53-- */
	/*  %.L53: [TAC] */
.main.L53:
	/*   jmp %.L54 [TAC] */
	jmp .main.L54
	/*  %.L52: [TAC] */
.main.L52:
	/*   %58 = const 7 [TAC] */
	movq $7, -264(%rbp)
	/*   print %58 [TAC] */
	movq -264(%rbp), %rdi
	callq __bx_print_int
	/*  %.L54: [TAC] */
.main.L54:
	/*   %62 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -272(%rbp)
	/*   %63 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -280(%rbp)
	/*   %64 = sub %62, %63 [TAC] */
	movq -272(%rbp), %r11
	subq -280(%rbp), %r11
	movq %r11, -288(%rbp)
	/*   jle %64, %.L59 [TAC] */
	jle .main.L59
	/*   jmp %.L60 [TAC] */
	/* --jmp .main.L60-- */
	/*  %.L60: [TAC] */
.main.L60:
	/*   jmp %.L61 [TAC] */
	jmp .main.L61
	/*  %.L59: [TAC] */
.main.L59:
	/*   %65 = const 8 [TAC] */
	movq $8, -296(%rbp)
	/*   print %65 [TAC] */
	movq -296(%rbp), %rdi
	callq __bx_print_int
	/*  %.L61: [TAC] */
.main.L61:
	/*   %69 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -304(%rbp)
	/*   %70 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -312(%rbp)
	/*   %71 = sub %69, %70 [TAC] */
	movq -304(%rbp), %r11
	subq -312(%rbp), %r11
	movq %r11, -320(%rbp)
	/*   jnl %71, %.L66 [TAC] */
	jnl .main.L66
	/*   jmp %.L67 [TAC] */
	/* --jmp .main.L67-- */
	/*  %.L67: [TAC] */
.main.L67:
	/*   jmp %.L68 [TAC] */
	jmp .main.L68
	/*  %.L66: [TAC] */
.main.L66:
	/*   %72 = const 9 [TAC] */
	movq $9, -328(%rbp)
	/*   print %72 [TAC] */
	movq -328(%rbp), %rdi
	callq __bx_print_int
	/*  %.L68: [TAC] */
.main.L68:
	/*   %76 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -336(%rbp)
	/*   %77 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -344(%rbp)
	/*   %78 = sub %76, %77 [TAC] */
	movq -336(%rbp), %r11
	subq -344(%rbp), %r11
	movq %r11, -352(%rbp)
	/*   jle %78, %.L73 [TAC] */
	jle .main.L73
	/*   jmp %.L74 [TAC] */
	/* --jmp .main.L74-- */
	/*  %.L74: [TAC] */
.main.L74:
	/*   jmp %.L75 [TAC] */
	jmp .main.L75
	/*  %.L73: [TAC] */
.main.L73:
	/*   %79 = const 10 [TAC] */
	movq $10, -360(%rbp)
	/*   print %79 [TAC] */
	movq -360(%rbp), %rdi
	callq __bx_print_int
	/*  %.L75: [TAC] */
.main.L75:
	/*   %84 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -368(%rbp)
	/*   %85 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -376(%rbp)
	/*   %86 = sub %84, %85 [TAC] */
	movq -368(%rbp), %r11
	subq -376(%rbp), %r11
	movq %r11, -384(%rbp)
	/*   jle %86, %.L80 [TAC] */
	jle .main.L80
	/*   jmp %.L83 [TAC] */
	/* --jmp .main.L83-- */
	/*  %.L83: [TAC] */
.main.L83:
	/*   %87 = copy %1 [TAC] */
	movq -16(%rbp), %r11
	movq %r11, -392(%rbp)
	/*   %88 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -400(%rbp)
	/*   %89 = sub %87, %88 [TAC] */
	movq -392(%rbp), %r11
	subq -400(%rbp), %r11
	movq %r11, -408(%rbp)
	/*   jle %89, %.L80 [TAC] */
	jle .main.L80
	/*   jmp %.L81 [TAC] */
	/* --jmp .main.L81-- */
	/*  %.L81: [TAC] */
.main.L81:
	/*   jmp %.L82 [TAC] */
	jmp .main.L82
	/*  %.L80: [TAC] */
.main.L80:
	/*   %90 = const 11 [TAC] */
	movq $11, -416(%rbp)
	/*   print %90 [TAC] */
	movq -416(%rbp), %rdi
	callq __bx_print_int
	/*  %.L82: [TAC] */
.main.L82:
	/*   %94 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -424(%rbp)
	/*   %95 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -432(%rbp)
	/*   %96 = sub %94, %95 [TAC] */
	movq -424(%rbp), %r11
	subq -432(%rbp), %r11
	movq %r11, -440(%rbp)
	/*   jz %96, %.L91 [TAC] */
	jz .main.L91
	/*   jmp %.L92 [TAC] */
	/* --jmp .main.L92-- */
	/*  %.L92: [TAC] */
.main.L92:
	/*   jmp %.L93 [TAC] */
	jmp .main.L93
	/*  %.L91: [TAC] */
.main.L91:
	/*   %97 = const 12 [TAC] */
	movq $12, -448(%rbp)
	/*   print %97 [TAC] */
	movq -448(%rbp), %rdi
	callq __bx_print_int
	/*  %.L93: [TAC] */
.main.L93:
	/*   %101 = const 0 [TAC] */
	movq $0, -456(%rbp)
	/*   jmp %.L102 [TAC] */
	/* --jmp .main.L102-- */
	/*  %.L102: [TAC] */
.main.L102:
	/*   %101 = const 1 [TAC] */
	movq $1, -456(%rbp)
	/*  %.L103: [TAC] */
.main.L103:
	/*   %104 = const 0 [TAC] */
	movq $0, -464(%rbp)
	/*   jmp %.L105 [TAC] */
	/* --jmp .main.L105-- */
	/*  %.L105: [TAC] */
.main.L105:
	/*   %104 = const 1 [TAC] */
	movq $1, -464(%rbp)
	/*  %.L106: [TAC] */
.main.L106:
	/*   %107 = sub %101, %104 [TAC] */
	movq -456(%rbp), %r11
	subq -464(%rbp), %r11
	movq %r11, -472(%rbp)
	/*   jz %107, %.L98 [TAC] */
	jz .main.L98
	/*   jmp %.L99 [TAC] */
	/* --jmp .main.L99-- */
	/*  %.L99: [TAC] */
.main.L99:
	/*   jmp %.L100 [TAC] */
	jmp .main.L100
	/*  %.L98: [TAC] */
.main.L98:
	/*   %108 = const 13 [TAC] */
	movq $13, -480(%rbp)
	/*   print %108 [TAC] */
	movq -480(%rbp), %rdi
	callq __bx_print_int
	/*  %.L100: [TAC] */
.main.L100:
	/*   %112 = const 0 [TAC] */
	movq $0, -488(%rbp)
	/*   jmp %.L113 [TAC] */
	/* --jmp .main.L113-- */
	/*  %.L113: [TAC] */
.main.L113:
	/*   %112 = const 1 [TAC] */
	movq $1, -488(%rbp)
	/*  %.L114: [TAC] */
.main.L114:
	/*   %115 = const 0 [TAC] */
	movq $0, -496(%rbp)
	/*   jmp %.L117 [TAC] */
	jmp .main.L117
	/*  %.L116: [TAC] */
.main.L116:
	/*   %115 = const 1 [TAC] */
	movq $1, -496(%rbp)
	/*  %.L117: [TAC] */
.main.L117:
	/*   %118 = sub %112, %115 [TAC] */
	movq -488(%rbp), %r11
	subq -496(%rbp), %r11
	movq %r11, -504(%rbp)
	/*   jz %118, %.L109 [TAC] */
	jz .main.L109
	/*   jmp %.L110 [TAC] */
	/* --jmp .main.L110-- */
	/*  %.L110: [TAC] */
.main.L110:
	/*   jmp %.L111 [TAC] */
	jmp .main.L111
	/*  %.L109: [TAC] */
.main.L109:
	/*   %119 = const 14 [TAC] */
	movq $14, -512(%rbp)
	/*   print %119 [TAC] */
	movq -512(%rbp), %rdi
	callq __bx_print_int
	/*  %.L111: [TAC] */
.main.L111:
	/*   %123 = const 0 [TAC] */
	movq $0, -520(%rbp)
	/*   jmp %.L125 [TAC] */
	jmp .main.L125
	/*  %.L124: [TAC] */
.main.L124:
	/*   %123 = const 1 [TAC] */
	movq $1, -520(%rbp)
	/*  %.L125: [TAC] */
.main.L125:
	/*   %126 = const 0 [TAC] */
	movq $0, -528(%rbp)
	/*   jmp %.L128 [TAC] */
	jmp .main.L128
	/*  %.L127: [TAC] */
.main.L127:
	/*   %126 = const 1 [TAC] */
	movq $1, -528(%rbp)
	/*  %.L128: [TAC] */
.main.L128:
	/*   %129 = sub %123, %126 [TAC] */
	movq -520(%rbp), %r11
	subq -528(%rbp), %r11
	movq %r11, -536(%rbp)
	/*   jz %129, %.L120 [TAC] */
	jz .main.L120
	/*   jmp %.L121 [TAC] */
	/* --jmp .main.L121-- */
	/*  %.L121: [TAC] */
.main.L121:
	/*   jmp %.L122 [TAC] */
	jmp .main.L122
	/*  %.L120: [TAC] */
.main.L120:
	/*   %130 = const 15 [TAC] */
	movq $15, -544(%rbp)
	/*   print %130 [TAC] */
	movq -544(%rbp), %rdi
	callq __bx_print_int
	/*  %.L122: [TAC] */
.main.L122:
	/*   %134 = const 0 [TAC] */
	movq $0, -552(%rbp)
	/*   jmp %.L136 [TAC] */
	jmp .main.L136
	/*  %.L135: [TAC] */
.main.L135:
	/*   %134 = const 1 [TAC] */
	movq $1, -552(%rbp)
	/*  %.L136: [TAC] */
.main.L136:
	/*   %137 = const 0 [TAC] */
	movq $0, -560(%rbp)
	/*   jmp %.L138 [TAC] */
	/* --jmp .main.L138-- */
	/*  %.L138: [TAC] */
.main.L138:
	/*   %137 = const 1 [TAC] */
	movq $1, -560(%rbp)
	/*  %.L139: [TAC] */
.main.L139:
	/*   %140 = sub %134, %137 [TAC] */
	movq -552(%rbp), %r11
	subq -560(%rbp), %r11
	movq %r11, -568(%rbp)
	/*   jz %140, %.L131 [TAC] */
	jz .main.L131
	/*   jmp %.L132 [TAC] */
	/* --jmp .main.L132-- */
	/*  %.L132: [TAC] */
.main.L132:
	/*   jmp %.L133 [TAC] */
	jmp .main.L133
	/*  %.L131: [TAC] */
.main.L131:
	/*   %141 = const 16 [TAC] */
	movq $16, -576(%rbp)
	/*   print %141 [TAC] */
	movq -576(%rbp), %rdi
	callq __bx_print_int
	/*  %.L133: [TAC] */
.main.L133:
	/*   %145 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -584(%rbp)
	/*   %146 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -592(%rbp)
	/*   %147 = sub %145, %146 [TAC] */
	movq -584(%rbp), %r11
	subq -592(%rbp), %r11
	movq %r11, -600(%rbp)
	/*   jz %147, %.L143 [TAC] */
	jz .main.L143
	/*   jmp %.L142 [TAC] */
	jmp .main.L142
	/*  %.L143: [TAC] */
.main.L143:
	/*   jmp %.L144 [TAC] */
	jmp .main.L144
	/*  %.L142: [TAC] */
.main.L142:
	/*   %148 = const 17 [TAC] */
	movq $17, -608(%rbp)
	/*   print %148 [TAC] */
	movq -608(%rbp), %rdi
	callq __bx_print_int
	/*  %.L144: [TAC] */
.main.L144:
	/*   %152 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -616(%rbp)
	/*   %153 = copy %0 [TAC] */
	movq -8(%rbp), %r11
	movq %r11, -624(%rbp)
	/*   %154 = sub %152, %153 [TAC] */
	movq -616(%rbp), %r11
	subq -624(%rbp), %r11
	movq %r11, -632(%rbp)
	/*   jnz %154, %.L150 [TAC] */
	jnz .main.L150
	/*   jmp %.L149 [TAC] */
	jmp .main.L149
	/*  %.L150: [TAC] */
.main.L150:
	/*   jmp %.L151 [TAC] */
	jmp .main.L151
	/*  %.L149: [TAC] */
.main.L149:
	/*   %155 = const 18 [TAC] */
	movq $18, -640(%rbp)
	/*   print %155 [TAC] */
	movq -640(%rbp), %rdi
	callq __bx_print_int
	/*  %.L151: [TAC] */
.main.L151:
	movq %rbp, %rsp
	popq %rbp
	xorl %eax, %eax
	retq
