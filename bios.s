.data
  led: .word 0xFFFFFC60
  digits: .word 0xFFFFFC00
  maxui: .word 0xFFFFFFFF
  beep: .word 0xFFFFFD10
  switch: .word 0xFFFFFC70
  enable_led: .word 0xFFFFFFFF
  kbd: .word 0xFFFFFC10

.text
  j start

sleep1s:
	sw 	$fp, 0($sp) 
	sw 	$t1, -4($sp) 
	sw 	$t2, -8($sp) 
	ori 	$fp, $sp, 0 
	addiu 	$sp, $fp, -20 
	# retval0: -12($fp) 
	# x: -16($fp) 
entry0:
	ori 	$t1, $zero, 0 
	sw 	$t1, -16($fp) 
whilecond0:
	lw 	$t1, -16($fp) 
	lui 	$t2, 0x14 
	ori 	$t2, $t2, 0 
	slt 	$t1, $t1, $t2 
	bne 	$t1, $zero, whilebody0 
	nop 
	j 	whileend0 
	nop 
whilebody0:
	lw 	$t2, -16($fp) 
	ori 	$t1, $zero, 1 
	addu 	$t1, $t2, $t1 
	sw 	$t1, -16($fp) 
	j 	whilecond0 
	nop 
whileend0:
	lw 	$t1, -16($fp) 
	sw 	$t1, -12($fp) 
	j 	return0 
	nop 
return0:
	lw 	$t1, -12($fp) 
	ori 	$v0, $t1, 0 
	lw 	$fp, 0($fp) 
	lw 	$t1, -4($fp) 
	lw 	$t2, -8($fp) 
	ori 	$sp, $fp, 0 
	jr 	$ra 
	nop 
	nop 
 
start:
  jal sleep1s
  addiu $t1, $t1, 1
  lw $t0, led($0)
  sw $t1, 0($t0)
  j start
  nop

done:
  nop
