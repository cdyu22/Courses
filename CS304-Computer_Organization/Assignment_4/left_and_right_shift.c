/*
//Multiply by 2 the amount of times we shift
for ( int i = 0; i < shift; i++ )
    accumulator *= 2;
*/

/*
//Convert the other
convert_to_binary(accumulator,main_bin.bin);
tracker = 0;
for (int i = 0; i < 19; i++)
{
    if (main_bin.bin[i] != '0' && main_bin.bin[i] != '1')
        continue;
    right_fill[tracker] = main_bin.bin[i];
    tracker++;
}

tracker = shift;
for (int j = 16; j > 0; j--)
    right_fill[j] = right_fill[j-tracker];

for (int k = 0; k < tracker; k++)
    right_fill[k] = right_fill[0];

tracker = 0;
for (int m = 0; m < 19; m++)
{
    if (m %5 == 4)
    {
        main_bin.bin[m] == ' ';
        continue;
    }
    main_bin.bin[m] = right_fill[tracker];
    tracker++;
}
accumulator = get_binary_op(main_bin.bin);
break;
*/
