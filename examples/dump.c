/*
 *  This library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public
 *  License as published by the Free Software Foundation; either
 *  version 2 of the License, or (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 *
 *  Copyright (C) 2008-2009 SlimLogic Ltd
 *  Authors: Liam Girdwood <lrg@slimlogic.co.uk>
 *           Stefan Schmidt <stefan@slimlogic.co.uk>
 */

#include <stdio.h>
#include "ascenario.h"

int main(int argc, char *argv[])
{
	if (argc != 2) {
		printf("usage: %s card (hw: prefix needed"
			" e.g. hw:CARD=0 or hw:Intel)\n", argv[0]);
		return 0;
	}

	return snd_scenario_dump(argv[1]);
}
